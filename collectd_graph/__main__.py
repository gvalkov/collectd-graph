#!/usr/bin/env python3
# -*- coding: utf-8; -*-

from __future__ import print_function
from __future__ import absolute_import

import os, sys
import optparse
import textwrap
import subprocess

from collections import ChainMap
from functools import partial

from . import __version__
from . import collectd, graphdef, utils


# List taken from the -a/--imgformat option of rrdgraph.
IMAGE_FORMATS = {
    'PNG', 'SVG', 'EPS', 'PDF', 'XML', 'XMLENUM',
    'JSON', 'JSONTIME', 'CSV', 'TSV', 'SSV'
}


def parseopt(argv=None):
    o = optparse.Option

    # The dryrun optionally accepts the 'json' argument.
    dryrun_callback = partial(utils.optional_value, optional='json')

    general_options = [
        o('-V', '--version', action='store_true', help='show version and exit'),
        o('-h', '--help',    action='store_true', help='show this help message and exit'),
        o('-n', '--dryrun',  action='callback',   help='print commands and exit',
          dest='dryrun', callback=dryrun_callback, default=False),
        o('-o', '--overrides', metavar='path',    help='graph definition overrides file')
    ]

    collectd_options = [
        o('-d', '--datadir',   metavar='path',      help='path to collectd rrd datadir'),
        o('-s', '--start',     metavar='timespec',  help='start time of time series'),
        o('-e', '--end',       metavar='timespec',  help='end time of time series data'),
        o('-S', '--step',      metavar='sec',       help='data resolution in seconds'),
        o('-a', '--imgformat', metavar='format',    help='image format for the generated graph'),
    ]

    prog = os.path.basename(sys.argv[0])
    prog = prog if prog != '__main__.py' else 'collectd-graph'

    description = ''

    epilog = r'''
    Commands:
      list
        Enumerate all plugins in -d/--datadir that this tool
        knows how to graph.

      graph <name> <output> [<name> <output> ...]
        Create graphs for the specified plugins.

    Environment variables:
      COLLECTD_GRAPH_DATADIR  path to collectd rrd datadir

    Image formats:
      PNG SVG EPS PDF XML XMLENUM JSON JSONTIME CSV TSV SSV

    Examples:
      {prog} -d /var/db/collectd list
      {prog} -s -2d graph a/memory/memory memory.png
      {prog} graph a/users/users users.png b/load/load load.png
    '''.format(prog=prog)

    parser = optparse.OptionParser(
        usage='%prog [options] <command> [<cmdargs> ...]',
        prog=prog,
        epilog=textwrap.dedent(epilog),
        formatter=utils.CompactHelpFormatter(),
        description=textwrap.dedent(description),
        add_help_option=False,
    )

    general_group = optparse.OptionGroup(parser, 'General Options')
    general_group.add_options(general_options)
    parser.add_option_group(general_group)

    collectd_group = optparse.OptionGroup(parser, 'Collectd Options')
    collectd_group.add_options(collectd_options)
    parser.add_option_group(collectd_group)

    if not argv:
        opts, args = parser.parse_args()
    else:
        opts, args = parser.parse_args(argv)

    return parser, opts, args


def read_graphdef_module(module):
    '''
    Read graph definitions from a module or dictionary.

    Parameters
    ----------
    module : module|dict
        A mapping of plugin names to rrdgraph definitions. See the
        'graphdef' module for more information on the expected
        contents of this mapping.

    Returns
    -------
    (dict, module|dict)
    '''

    # This can be a module, i.e. 'collectd_graph.graphdef', or a
    # dictionary, such as the one returned by 'read_overrides_file()'.
    module = getattr(module, '__dict__', module)

    definitions = {
        'stacked': {},
        'single':  {},
    }

    for name, value in module.items():
        if isinstance(value, str):
            value = value.strip()
        if name.startswith('stacked_graph_'):
            definitions['stacked'][name[14:]] = value
        elif name.startswith('graph_'):
            definitions['single'][name[6:]] = value

    return definitions, module


def read_overrides_file(path):
    '''
    Execute a file and returns the resulting globals as a dictionary.
    '''
    code = compile(open(path).read(), path, 'exec')
    namespace = {}
    exec(code, namespace, namespace)
    return read_graphdef_module(namespace)


def imgformat_from_name(path, formats=IMAGE_FORMATS):
    root, ext = os.path.splitext(path)
    ext = ext.lstrip('.')
    if ext.upper() in formats:
        return ext.upper()


def cmd_graph(opts, names, args):
    if not args:
        msg = 'error: no plugins specified (hint: see output of "list" command)'
        raise SystemExit(msg, 2)

    plugins = utils.pairwise(args)

    for plugin, output in plugins:
        if not output:
            msg = 'error: no output specified for plugin %r' % plugin
            raise SystemExit(msg, 2)

    commands = []
    for plugin, output in plugins:
        if plugin not in names:
            raise SystemExit('error: "%s" is not a known plugin type' % plugin, 1)

        if not opts.imgformat:
            opts.imgformat = imgformat_from_name(output)

        if not opts.imgformat:
            msg = 'error: could not determine output format from %r and -a/--imgformat not set' % output
            raise SystemExit(msg, 2)

        type, defn, stat = names[plugin]
        defn = defn.format(file=stat.path, colors=collectd.default_colors)
        cmd = collectd.rrdgraph_cmd(output, opts.imgformat, defn.splitlines())
        commands.append(cmd)

    if opts.dryrun and opts.dryrun == 'json':
        import json
        print(json.dumps(commands, indent=2))
        return 0

    for cmd in commands:
        if opts.dryrun:
            print(utils.shlex_join(cmd))
            continue

        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = proc.communicate()

        if proc.returncode != 0:
            err = err.decode('utf8').rstrip('\n').splitlines()
            msg = ['error: rrdgraph return non-zero exit status (stderr will follow)']
            msg += ('>  %s' % line for line in err)
            raise SystemExit('\n'.join(msg), 2)

    return 0


def cmd_list(opts, names):
    '''
    Prints all plugins that can be graphed by this tool.
    '''
    for name in sorted(names):
        graphtype, _, _ = names[name]
        if graphtype == 'single':
            print(name)
        elif graphtype == 'stacked':
            print(name, '(stacked)')


def main(argv=sys.argv):
    parser, opts, args = parseopt(argv)
    args = args[1:]

    if opts.help or len(argv) == 1:
        parser.print_help()
        return 0

    if opts.version:
        print('collectd-graph version %s' % __version__)
        return 0

    if not args:
        raise SystemExit('error: no command specified', 1)

    if args[0] not in {'list', 'graph'}:
        msg = 'error: "%s" is not a valid collectd-graph command' % args[0]
        raise SystemExit(msg, 1)

    if not opts.datadir and os.environ.get('COLLECTD_GRAPH_DATADIR'):
        opts.datadir = os.environ.get('COLLECTD_GRAPH_DATADIR')

    if not opts.datadir:
        msg = 'error: the -d/--datadir option or COLLECTDGRAPH_DATADIR environment variable must be set'
        raise SystemExit(msg, 1)

    if opts.imgformat and opts.imgformat.upper() not in IMAGE_FORMATS:
        msg = 'error: unknown output image format %r' % opts.imgformat.upper()
        raise SystemExit(msg, 1)

    definitions, _ = read_graphdef_module(graphdef)
    default_colors = collectd.default_colors
    graph_colors = {}

    if opts.overrides:
        overrides, module = read_overrides_file(opts.overrides)
        definitions = ChainMap(overrides, definitions)

        if 'default_colors' in module:
            default_colors = ChainMap(module['default_colors'], default_colors)

        if 'graph_colors' in module:
            graph_colors = ChainMap(module['graph_colors'], graph_colors)

    # Find all rrd files in the datadir and wrap them in a collectd.Statistic object.
    stats = collectd.list_datadir(opts.datadir)

    matched = collectd.match_stats(stats, definitions)

    names = {}
    for stat, graphtype, gdef in matched:
        if graphtype == 'single':
            key = os.path.relpath(stat.path, opts.datadir)[:-4]
        elif graphtype == 'stacked':
            key = stat[0].title
        names[key] = (graphtype, gdef, stat)

    if 'graph' in args:
        return cmd_graph(opts, names, args[1:])

    if 'list' in args:
        return cmd_list(opts, names)


def _main(argv=sys.argv):
    try:
        ret = main(argv)
    except SystemExit as error:
        if not isinstance(error.args, tuple):
            raise  # re-raise the exception

        msg, code = error.args
        print(msg, file=sys.stderr)
        sys.exit(code)
    sys.exit(ret)


if __name__ == '__main__':
    _main()
