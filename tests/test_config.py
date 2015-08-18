# -*- coding: utf-8; -*-


from collectd_graph import utils
from collectd_graph.collectd import Statistic as S


def test_ordered():
    order = ['free', 'cached', 'buffered', 'used']
    stats = ['buffered', 'apple', 'cached', 'free', 'zebra', 'slab_recl', 'slab_unrecl', 'used']

    res = utils.ordered(stats, *order, key=lambda x: x)
    exp = ['free', 'cached', 'buffered', 'used', 'apple', 'slab_recl', 'slab_unrecl', 'zebra']
    assert res == exp

    res = utils.ordered(stats, *order, unknown_first=True, key=lambda x: x)
    exp = ['apple', 'slab_recl', 'slab_unrecl', 'zebra', 'free', 'cached', 'buffered', 'used']
    assert res == exp


def test_match():
    pass
