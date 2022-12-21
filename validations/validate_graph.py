from queue import Queue
from typing import Tuple, Optional

from utils.graph_utils import input_to_adjacency_list


def validate_graph(input_graph: str, weighted=True) -> Tuple[bool, Optional[str]]:
    """
    Validates the input graph

    Example input:
    6 8
    0 1 3
    0 2 1
    0 3 8
    1 2 2
    1 4 5
    2 3 4
    2 4 5
    2 5 6
    :param input_graph: The input graph
    :param weighted: Whether the graph is weighted or not

    :return: A tuple with a boolean and a message. If the boolean is True, the graph is valid.
    If the boolean is False, then the graph is not valid and the message contains the reason.
    """
    lines = input_graph.splitlines()

    if len(lines) == 0:
        return False, "The input graph cannot be empty"

    if len(lines[0].split()) != 2:
        return False, "The first line must contain two integers specifying the number of nodes and edges"

    n, m = lines[0].split()

    if not n.isdigit() or not m.isdigit():
        return False, "The first line must contain two integers specifying the number of nodes and edges"

    n, m = int(n), int(m)
    if n < 1 or m < 0:
        return False, "The number of nodes must be at least 1 and the number of edges must be at least 0"

    lines = lines[1:]

    if len(lines) != m:
        return False, "The number of edges does not match the number of defined edges"

    for line in lines:

        if weighted:
            if len(line.split()) != 3:
                return False, f"The line {line} does not contain three values specifying the edge"

            u, v, w = line.split()
            if not u.isdigit() or not v.isdigit() or not w.isdigit():
                return False, f"The line {line} does not contain three integers specifying the edge"

            if int(w) <= 0:
                return False, f"The weight of the edge {line} must be positive"

        else:
            if len(line.split()) != 2:
                return False, f"The line {line} does not contain two values specifying the edge"

            u, v = line.split()
            if not u.isdigit() or not v.isdigit():
                return False, f"The line {line} does not contain two integers specifying the edge"

        u, v = int(u), int(v)

        if u == v:
            return False, f"The line {line} contains a edge from a node to itself"

        if u < 0 or u >= n or v < 0 or v >= n:
            return False, f"The line {line} contains an invalid node"

    return True, None

def validate_only_one_component(input_graph: str, directed: bool, weighted: bool) -> Tuple[bool, Optional[str]]:
    """
    First, validates the input graph. If the input graph is valid, it checks if the graph is connected.

    :param input_graph: The input graph
    :param directed: Whether the graph is directed or not
    :param weighted: Whether the graph is weighted or not
    :return: A tuple with a boolean and a message. If the boolean is True, the graph is valid.
    If the boolean is False, then the graph is not valid and the message contains the reason.
    """

    is_a_valid_graph, message = validate_graph(input_graph, weighted)

    if not is_a_valid_graph:
        return False, message

    graph = input_to_adjacency_list(input_graph, directed, weighted)

    visited = [False] * len(graph)
    queue = Queue()
    queue.put(0)

    while not queue.empty():
        node = queue.get()
        visited[node] = True

        for (neighbour, _) in graph[node]:
            if not visited[neighbour]:
                queue.put(neighbour)

    if all(visited):
        return True, None
    else:
        return False, "The graph must only have one connected component"

def validate_number_of_edges(n: int, m: int) -> Tuple[bool, Optional[str]]:
    """
    Validates the number of edges in relation to the number of nodes
    :param n: The number of nodes
    :param m: The number of edges
    :return: A tuple with a boolean and a message. If the boolean is True, the number of edges is valid.
    Otherwise, the message contains the reason.
    """
    if n-1 > m:
        return False, "The number of edges is not enough to connect all the nodes"

    if m > n*(n-1) / 2:
        return False, "The number of edges is too high"

    return True, None




