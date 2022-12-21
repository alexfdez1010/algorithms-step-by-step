from typing import List, Union, Tuple, Set
from graphviz import Digraph, Graph

from data_structures.disjoint_set_union import DisjointSetUnion


def draw_graph(n: int, edges: List[Union[Tuple[int, int], Tuple[int, int, float]]],
               weighted: bool = True,
               directed: bool = True,
               edges_selected: Set[Tuple[int,int]] = None) -> Graph:

    if edges_selected is None:
        edges_selected = []
        color = "black"
    else:
        color = "red"

    graph = Graph() if not directed else Digraph()

    for i in range(n):
        graph.node(str(i), shape="circle")

    if directed:

        for edge in edges:
            if edge in edges_selected:
                graph.edge(str(edge[0]), str(edge[1]), label=str(edge[2]) if weighted else "", color="green")
            else:
                graph.edge(str(edge[0]), str(edge[1]), label=str(edge[2]) if weighted else "", color=color)

    else:

        for edge in edges:

            if edge[0] >= edge[1]:
                continue

            if (edge[0], edge[1]) in edges_selected or (edge[1], edge[0]) in edges_selected:
                graph.edge(str(edge[0]), str(edge[1]), label=str(edge[2]) if weighted else "", color="green")
            else:
                graph.edge(str(edge[0]), str(edge[1]), label=str(edge[2]) if weighted else "", color=color)

    return graph

def draw_disjoint_sets(disjoint_set: DisjointSetUnion) -> Digraph:
    graph = Digraph()

    for i in range(disjoint_set.size()):
        graph.node(str(i), shape="circle")

    for (element, value) in enumerate(disjoint_set.sets):
        if element != value:
            graph.edge(str(element), str(value))

    return graph
