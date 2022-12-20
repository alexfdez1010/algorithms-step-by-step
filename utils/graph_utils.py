
from typing import List, Tuple, Union, Optional


def input_to_adjacency_list(input_string: str,
                            directed: bool = True,
                            weighted: bool = True) -> Optional[Union[List[List[int]], List[List[Tuple[int, float]]]]]:
    if weighted:
        return input_to_adjacency_list_weighted(input_string, directed)
    else:
        return input_to_adjacency_list_not_weighted(input_string, directed)


def input_to_adjacency_list_weighted(input_string: str,
                                     directed: bool = True) -> List[List[Tuple[int, float]]]:
    lines = input_string.splitlines()

    n, m = map(int, lines[0].split(" "))
    adjacency_list: List[List[Tuple[int, float]]] = [[] for _ in range(n)]

    lines = lines[1:]

    for edge in lines:
        u, v, w = edge.split()
        u, v, w = int(u), int(v), float(w)

        adjacency_list[u].append((v, w))

        if not directed:
            adjacency_list[v].append((u, w))

    return adjacency_list


def input_to_adjacency_list_not_weighted(input_string: str,
                                         directed: bool = True) -> List[List[int]]:
    lines = input_string.splitlines()

    n, m = map(int, lines[0].split(" "))
    adjacency_list: List[List[int]] = [[] for _ in range(n)]

    lines = lines[1:]

    for edge in lines:
        u, v = map(int, edge.split(""))
        adjacency_list[u].append(v)

        if not directed:
            adjacency_list[v].append(u)

    return adjacency_list

def adjacency_list_to_list_of_edges(adjacency_list: List[List[Union[int, Tuple[int, float]]]]) \
        -> List[Union[Tuple[int, int], Tuple[int, int, float]]]:
    edges = []
    for u in range(len(adjacency_list)):
        for v in adjacency_list[u]:
            if isinstance(v, tuple):
                edges.append((u, v[0], v[1]))
            else:
                edges.append((u, v))
    return edges


