from queue import PriorityQueue
from typing import Union, List, Tuple, Set

from graphviz import Graph

from utils.draw_utils import draw_graph
from utils.graph_utils import input_to_adjacency_list, adjacency_list_to_list_of_edges
from utils.markdown_utils import latex_to_markdown, matrix_to_markdown


def dijkstra(input_graph: str) -> Union[str, Graph]:
    input_graph = input_graph.splitlines()
    u = int(input_graph[-1])
    input_graph = input_graph[:-1]
    input_graph = "\n".join(input_graph)

    graph: List[List[Tuple[int, float]]] = input_to_adjacency_list(input_graph, directed=False, weighted=True)

    edge_list = adjacency_list_to_list_of_edges(graph)

    yield "## Dijkstra's algorithm resolution"
    yield "The initial graph is the following:"
    yield draw_graph(len(graph), edge_list, weighted=True, directed=False)
    yield f"The source vertex is {u}. From this vertex, we will calculate the shortest path to all other vertices."

    queue = PriorityQueue()
    distances = [float('inf')] * len(graph)
    previous_nodes = [-1] * len(graph)
    distances[u] = 0

    for edge in graph[u]:
        distances[edge[0]] = edge[1]
        previous_nodes[edge[0]] = u
        queue.put((edge[1], edge[0]))
        yield f"Added the edge {edge[0]} with distance {edge[1]} to the priority queue\n"

    yield f"The initial distances from the node {u} are:\n"
    yield latex_to_markdown(matrix_to_markdown([distances]))

    counter = 1
    while not queue.empty():
        distance, node = queue.get()

        yield f"### Step {counter}\n"
        yield f"Removed the edge with distance {distance} and node {node} from the priority queue\n"
        counter += 1

        for edge in graph[node]:

            new_distance = distances[node] + edge[1]
            if distances[edge[0]] > new_distance:
                yield f"Updated the distance to the node {edge[0]} from {distances[edge[0]]} to {new_distance}\n"
                yield f"Added the edge {edge[0]} with distance {distances[edge[0]]} to the priority queue\n"
                distances[edge[0]] = distances[node] + edge[1]
                previous_nodes[edge[0]] = node
                queue.put((distances[edge[0]], edge[0]))

        yield f"The distances from the node {u} are:\n"
        yield latex_to_markdown(matrix_to_markdown([distances]))
        yield f"The edges selected are (green):\n"
        yield draw_graph(
            len(graph), edge_list, weighted=True, directed=False, edges_selected=__get_edges_selected(previous_nodes)
        )

    yield f"### Result\n"
    yield f"The final distances from the node {u} are:\n"
    yield latex_to_markdown(matrix_to_markdown([distances]))
    yield f"The edges that define the minimum paths are marked in green:\n"
    yield draw_graph(
        len(graph), edge_list, weighted=True, directed=False, edges_selected=__get_edges_selected(previous_nodes)
    )


def __get_edges_selected(previous_nodes) -> Set[Tuple[int, int]]:
    edges_selected = set()

    for i in range(len(previous_nodes)):
        if previous_nodes[i] != -1:
            edges_selected.add((previous_nodes[i], i))

    return edges_selected
