# -*- coding: utf-8 -*-
"""A simple pathfinding package.
"""
import algorithms
import metrics
import nodes
import load_map
try:
    from pathfinding import test
except ImportError:
    _exp = []
else:
    _exp = ['test']

__all__ = ['algorithms', 'metrics', 'nodes', 'load_map'] + _exp