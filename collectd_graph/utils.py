# -*- coding: utf-8; -*-

import os
import sys
import shlex
import subprocess

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


def ordered(it, *order, unknown_first=False, key=None):
    '''
    Sort collection, while maintaining order of certain elements.

    >>> nums = [3, 7, 8, 1, 9, 5, 2, 6, 4]
    >>> ordered(nums, 1, 2, 3, 4, 5)
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> ordered(nums, 1, 2, 3, 4, 5, unknown_first=True)
    [5, 6, 7, 8, 9, 1, 2, 3, 4]
    '''

    # @todo: This is specific to Statistic objects.
    key = key if key else attrgetter('type_instance')
    order = {i: n for n, i in enumerate(order)}

    # First sort all elements alpha-numerically.
    res = sorted(it, key=key)
    idx = -1 if unknown_first else len(order)

    def order_key(el):
        return order[key(el)] if key(el) in order else idx

    res = sorted(res, key=order_key)
    return res


def shlex_join(it, sep=' '):
    '''
    Join a list of string in to a shell-safe string. Opposite of
    shlex.split().
    '''
    return sep.join(shlex.quote(i) for i in it)


def pairwise(it, size=2, fillvalue=None):
    '''
    Split an iterable into n-sized parts.

    >>> pairwise(range(10))
    >>> [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)]

    >>> pairwise(range(10), size=3)
    >>> [(0, 1, 2), (3, 4, 5), (6, 7, 8), (9, None, None)]
    '''
    it = iter(it)
    return list(zip_longest(*([it] * size), fillvalue=fillvalue))


def openfile(path):
    '''Open a file or URL in the user's preferred application.'''

    if sys.platform in {'linux', 'linux2'}:
        cmd = ['xdg-open', path]
    elif sys.platform == 'dawin':
        cmd = ['open', path]
    elif sys.platform == 'win32':
        return os.startfile(path)

    return subprocess.check_call(cmd)
