from queue import PriorityQueue
from random import randint
from typing import Union, List, Optional

from graphviz import Graph

from utils.draw_utils import draw_graph
from utils.graph_utils import input_to_adjacency_list, adjacency_list_to_list_of_edges


def prim_algorithm(input_string: str) -> Optional[List[Union[str, Graph]]]:
    """
    Prim's algorithm is a greedy algorithm that finds a minimum spanning tree for a weighted undirected graph.
    :param input_string: The string representation of the graph.
    :return: A list with the elements to render in the frontend that represent the resolution of the algorithm.
    """

    graph = input_to_adjacency_list(input_string, directed=False, weighted=True)

    edge_list = adjacency_list_to_list_of_edges(graph)

    yield "# Prim's algorithm resolution"
    yield "The initial graph is the following:"
    yield draw_graph(len(graph), edge_list, weighted=True, directed=False)

    set_visited = set()
    edges_selected = set()
    queue = PriorityQueue()

    node = randint(0, len(graph) - 1)
    yield f"Starting from the node {node} selected randomly\n"

    set_visited.add(node)
    step = 1

    u, v, weight = None, None, None

    total_weight = 0
    while len(set_visited) < len(graph):

        yield f"### Step {step}\n"
        for (neighbor, weight) in graph[node]:
            if neighbor not in set_visited:
                yield f"Added the edge from {node} to {neighbor} with weight {weight} to the priority queue\n"
                queue.put((weight, (node, neighbor)))

        while not queue.empty():
            weight, (u, v) = queue.get()
            if v not in set_visited:
                break

        set_visited.add(v)
        edges_selected.add((u, v))
        total_weight += weight
        node = v

        yield f"Added the edge from {u} to {v} with weight {weight} to the MST\n"
        yield f"The nodes visited are: {set_visited}\n"
        yield draw_graph(len(graph), edge_list, weighted=True, directed=False, edges_selected=edges_selected)
        step += 1

    yield "### Final result\n"
    yield "The final graph is the following:"
    yield draw_graph(len(graph), edge_list, weighted=True, directed=False, edges_selected=edges_selected)
    yield f"The total weight of the MST is {total_weight}"
