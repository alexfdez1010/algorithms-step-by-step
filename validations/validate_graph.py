from queue import Queue

from utils.graph_utils import input_to_adjacency_list


def validate_graph(input_graph, weighted=True):
    lines = input_graph.splitlines()

    if len(lines) == 0:
        return False

    if len(lines[0].split()) != 2:
        return False

    n, m = lines[0].split()

    if not n.isdigit() or not m.isdigit():
        return False

    n, m = int(n), int(m)
    if n < 1 or m < 0:
        return False

    lines = lines[1:]

    if len(lines) != m:
        return False

    for line in lines:

        if weighted:
            if len(line.split()) != 3:
                return False

            u, v, w = line.split()
            if not u.isdigit() or not v.isdigit() or not w.isdigit():
                return False
        else:
            if len(line.split()) != 2:
                return False
            u, v = line.split()
            if not u.isdigit() or not v.isdigit():
                return False

        u, v = int(u), int(v)
        if u < 0 or u >= n or v < 0 or v >= n:
            return False

    return True

def validate_only_one_component(input_graph, directed, weighted):

    if not validate_graph(input_graph, weighted):
        return False

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

    return all(visited)

def validate_number_of_edges(n: int, m: int):
    return n-1 <= m <= n * (n - 1) / 2




