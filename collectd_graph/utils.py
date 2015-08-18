# -*- coding: utf-8; -*-

import shlex

from operator import attrgetter
from optparse import IndentedHelpFormatter

try:
    from itertools import izip_longest as zip_longest
except ImportError:
    from itertools import zip_longest


class CompactHelpFormatter(IndentedHelpFormatter):
    '''A more compact option-help formatter.'''

    def __init__(self, *args, **kw):
        super(CompactHelpFormatter, self).__init__(*args, **kw)
        self.max_help_position = 40
        self.indent_increment = 1

    def format_option_strings(self, option):
        '''
        >>> _format_option_strings(('-f', '--format'))
        -f, --format arg
        '''

        opts = []

        if option._short_opts:
            opts.append(option._short_opts[0])
        if option._long_opts:
            opts.append(option._long_opts[0])
        if len(opts) > 1:
            opts.insert(1, ', ')
        if option.takes_value():
            metavar = option.metavar or 'arg'
            opts.append(' <%s>' % metavar)

        return ''.join(opts)

    def format_heading(self, heading):
        return '' if heading == 'Options' else heading + ':\n'

    def format_epilog(self, epilog):
        return epilog if epilog else ''


def optional_value(option, optstr, value, parser, optional):
    '''
    An optparse option callback, with an optional value. For example:

       Option('-n', '--dryrun', default=False, action='callback',
              callback=partial(optional_value, optional='json'))

    Allows the following constructs on the command-line:
       -n|--dryrun             => options.dryrun == True
       -n json | --dryrun=json => options.dryrun == 'json'
       -n yaml | --dryrun=yaml => options.dryrun == False
    '''
    value = option.default

    for arg in parser.rargs:
        if arg == optional:
            value = arg
            break
    else:
        value = True

    if value == optional:
        del parser.rargs[:1]
    setattr(parser.values, option.dest, value)


def ordered(stats, *order, unknown_first=False, key=None):
    key = key if key else attrgetter('type_instance')
    order = {i: n for n, i in enumerate(order)}

    # First sort all elements alphanumerically.
    res = sorted(stats, key=key)

    idx = -1 if unknown_first else len(order)
    order_key = lambda x: order[key(x)] if key(x) in order else idx
    res = sorted(res, key=order_key)
    return res


def shlex_join(it, sep=' '):
    return sep.join(shlex.quote(i) for i in it)


def pairwise(it, size=2, fillvalue=None):
    it = iter(it)
    return list(zip_longest(*([it] * size), fillvalue=fillvalue))
