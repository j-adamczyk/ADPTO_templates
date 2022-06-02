import math
from itertools import combinations
from typing import Iterable

from lab7_tree_decomposition_vertex_cover_size.vertex_cover.types import (
    VertexSets,
    TreeDecomposition,
)


def check_subgraph_VC(
    graph: VertexSets, vertices_subset: Iterable[int], candidate_vertices: Iterable[int]
) -> bool:
    """
    Answers the question: if for given graph we check the subgraph given by the
    vertices subset, does the set of candidate vertices create a Vertex Cover
    for this subgraph?

    :param graph: graphs represented as a list of sets (incident vertices)
    :param vertices_subset: vertices of subgraph
    :param candidate_vertices: candidate solution for Vertex Cover
    :returns: whether candidate vertices are a Vertex Cover solution for subgraph
    """
    pass


# map set of vertices (vertex cover) to its size (or infinity if it's not VC)
memoization_table = {}


def f(graph: VertexSets, bags: TreeDecomposition, bag_idx: int, vertex_cover: set[int]) -> int:
    # check memoization table, update if we don't have Vertex Cover
    global memoization_table

    # create memoization key from vertex cover


    # if bag_idx bag vertices don't create vertex cover, set table value to infinity


    # if we have key in table, return value


    # if we may have Vertex Cover, and we don't have memoized value, calculate

    # k = |C|
    k = len(vertex_cover)

    # go through each child, for each one select the smallest addition to the
    # parent's Vertex Cover
    for child_idx in bags[bag_idx].children:
        # set of vertices that are in child, but were not in parent, so they
        # are new and have to be considered
        child_new = None

        # set of vertices common for child and current Vertex Cover
        common = None

        # recursively check each subset of child new vertices (that were not
        # in the parent), and  select the smallest addition to Vertex Cover
        best = math.inf

        k += best - len(common)

    # memoize calculated result for key


    return k


def vertex_cover_size(graph: VertexSets, tree_decomp: TreeDecomposition) -> int:
    """
    Calculates size of minimal Vertex Cover for given graph, using its tree
    decomposition.

    :param graph: graphs represented as a list of sets (incident vertices)
    :param tree_decomp: tree decomposition of graph
    :returns: size of minimal Vertex Cover
    """
    best_k = math.inf

    # decomposition tree root vertices
    bag = tree_decomp[1].bag

    # check all combinations of all sizes, choose best (smallest) vertex cover size

    return best_k
