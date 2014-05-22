from __future__ import print_function, division
import numpy as np
import networkx as nx

def timedelta64_to_secs(timedelta):
    """Convert `timedelta` to seconds.

    Parameters
    ----------
    timedelta : np.timedelta64

    Returns
    -------
    float : seconds
    """
    if len(timedelta) == 0:
        return np.array([])
    else:
        return timedelta / np.timedelta64(1, 's')

def tree_root(graph):
    """Returns the object that is the root of the tree.

    Parameters
    ----------
    graph : networkx.Graph
    """
    # from http://stackoverflow.com/a/4123177/732596
    assert isinstance(graph, nx.Graph)
    roots = [n for n,d in graph.in_degree_iter() if d==0]
    assert len(roots) < 2, 'Tree has more than one root!'
    assert len(roots) == 1, 'Tree has no root!'
    return roots[0]

def nodes_adjacent_to_root(graph):
    root = tree_root(graph)
    return graph.successors(root)

def index_of_column_name(df, name):
    for i, col_name in enumerate(df.columns):
        if col_name == name:
            return i
    raise KeyError(name)
