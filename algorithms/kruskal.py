from typing import Union

from graphviz import Graph, Digraph

from data_structures.disjoint_set_union import DisjointSetUnion
from utils.draw_utils import draw_graph, draw_disjoint_sets
from utils.graph_utils import input_to_adjacency_list, adjacency_list_to_list_of_edges


def kruskal_algorithm(input_graph: str) -> Union[str, Graph, Digraph]:
    """
    Kruskal's algorithm for finding the minimum spanning tree of a graph
    :param input_graph: string representation of the graph
    :return: A list with the elements to render in the frontend that represent the resolution of the algorithm.
    """

    graph = input_to_adjacency_list(input_graph, directed=False, weighted=True)

    edge_list = adjacency_list_to_list_of_edges(graph)

    yield "## Kruskal's algorithm resolution"
    yield "The initial graph is the following:"
    yield draw_graph(len(graph), edge_list, weighted=True, directed=False)

    dsu = DisjointSetUnion(len(graph))
    yield "The initial Disjoint Set Union is the following:"
    yield draw_disjoint_sets(dsu)

    edges_selected = set()
    total_weight = 0

    edge_list = list(filter(lambda x: x[0] < x[1], edge_list))

    edge_list.sort(key=lambda x: x[2])
    yield "The edges of the graph sorted by weight are the following:"
    yield " | ".join([f"({edge[0]}, {edge[1]})" for edge in edge_list])

    edge_index = 0

    while len(edges_selected) < len(graph) - 1 and edge_index < len(edge_list):

        u, v, weight = edge_list[edge_index]

        yield f"### Step {edge_index + 1}\n"

        if dsu.find(u) != dsu.find(v):
            dsu.union(u, v)
            edges_selected.add((u, v))
            total_weight += weight

            yield f"The edge ({u}, {v}) is added to the MST"
            yield f"The total weight of the MST is {total_weight}"
            yield draw_graph(len(graph), edge_list, weighted=True, directed=False, edges_selected=edges_selected)
            yield "The current state of the Disjoint Set Union is the following:"
            yield draw_disjoint_sets(dsu)

        else:
            yield f"The edge is discarded as {u} and {v} are already in the same set"

        edge_index += 1

    yield "## Final result\n"
    yield "The final graph is the following:"
    yield draw_graph(len(graph), edge_list, weighted=True, directed=False, edges_selected=edges_selected)
    yield f"The total weight of the MST is {total_weight}"
