# -*- coding: utf-8; -*-

from __future__ import absolute_import

import os
import re
import textwrap

from fnmatch import fnmatch
from collections import namedtuple, defaultdict

from . import utils


time_map = {
    'hour': 3600,
    'day':  86400,
    'week':    7 * 86400,
    'month':  31 * 86400,
    'year':  366 * 86400,
    'h': 3600,
    'd': 86400,
    'w':   7 * 86400,
    'm':  31 * 86400,
    'y': 366 * 86400.
}

default_colors = {
    'Canvas':        'FFFFFF',

    'FullRed':       'FF0000',
    'FullGreen':     '00E000',
    'FullBlue':      '0000FF',
    'FullYellow':    'F0A000',
    'FullCyan':      '00A0FF',
    'FullMagenta':   'A000FF',

    'HalfRed':       'F7B7B7',
    'HalfGreen':     'B7EFB7',
    'HalfBlue':      'B7B7F7',
    'HalfYellow':    'F3DFB7',
    'HalfCyan':      'B7DFF7',
    'HalfMagenta':   'DFB7F7',

    'HalfBlueGreen': '89B3C9',
}


_Statistic = namedtuple('Statistic', 'path, host, plugin, plugin_instance, type, type_instance')

class Statistic(_Statistic):
    @property
    def title(self):
        if self.plugin_instance:
            fmt = '{self.host}/{self.plugin}-{self.plugin_instance}/{self.type}'
        else:
            fmt = '{self.host}/{self.plugin}/{self.type}'
        return fmt.format(self=self)


def rglob(path, pattern):
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch(name, pattern):
                yield os.path.join(root, name)


def list_datadir(datadir):
    '''Wraps every rrd file in the collectd datadir in a Statistic object.'''

    for path in rglob(datadir, '*.rrd'):
        relpath = os.path.relpath(path, datadir)
        relpath = relpath.replace('.rrd', '')

        host, plugin, p_type = relpath.split('/')
        plugin, _, plugin_instance = plugin.partition('-')
        p_type, _, p_type_instance = p_type.partition('-')

        stat = Statistic(path, host, plugin, plugin_instance, p_type, p_type_instance)
        yield stat


def match_stats(stats, definitions):
    by_plugin = defaultdict(list)
    for stat in stats:
        by_plugin[stat.plugin].append(stat)

    matches = {
        'callable': defaultdict(list),
        'single':   defaultdict(list),
        'stacked':  defaultdict(list),
    }

    for plugin, value in definitions['single'].items():
        if plugin in by_plugin:
            for stat in by_plugin[plugin]:
                yield stat, 'single', value

    for plugin, value in definitions['stacked'].items():
        if plugin in by_plugin:
            stats = by_plugin[plugin]
            yield stats, 'stacked', value


def sanitize_type_instance(name):
    name = re.sub(r'[^A-Za-z0-9\-_]', '_', name)
    return name


def graph_generic_stack(stats, opts):
    rrdargs = []

    if 'title' in opts:
        rrdargs += ['-t', opts['title']]

    if 'rrd_args' in opts:
        rrdargs += opts['rrd_args']

    if 'field_order' in opts:
        stats = utils.ordered(stats, opts['field_order'])

    vname = None
    for n, stat in enumerate(stats):
        vname = str(n) + sanitize_type_instance(stats.type_instance)

        defs = r'''
        DEF:{vname}_min={file}:value:MIN
        DEF:{vname}_avg={file}:value:AVERAGE
        DEF:{vname}_max={file}:value:MAX
        CDEF:{vname}_nnl={vname}_avg,UN,0,{vname}_avg,IF
        '''

        defs = defs.format(vname=vname, file=stat.file)
        defs = textwrap.dedent(defs.strip())
        rrdargs += defs.splitlines()

    cdef = 'CDEF:${vname}_stk=${vname}_nnl'
    rrdargs.append(cdef)


def rrdgraph_cmd(output, imgformat, args, rrdtool='rrdtool'):
    cmd = [rrdtool, 'graph', output, '--imgformat', imgformat]
    cmd.extend(args)
    return cmd
