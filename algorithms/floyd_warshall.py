from utils.draw_utils import draw_graph
from utils.graph_utils import input_to_adjacency_list, adjacency_list_to_list_of_edges
from utils.markdown_utils import matrix_to_markdown, latex_to_markdown


def floyd_warshall(input_graph):
    """
    Computes the shortest path between all pairs of nodes in a graph.
    :param input_graph: The graph.
    :return: The shortest path between all pairs of nodes in a graph.
    """
    graph = input_to_adjacency_list(input_graph, directed=True, weighted=True)
    edge_list = adjacency_list_to_list_of_edges(graph)

    n = len(graph)
    distance = [[float('inf') for _ in range(n)] for _ in range(n)]

    for i in range(n):
        distance[i][i] = 0

    for u in range(n):
        for v, w in graph[u]:
            distance[u][v] = w

    yield "## Floyd-Warshall Algorithm resolution"
    yield "The graph is:"
    yield draw_graph(len(graph), edge_list, weighted=True, directed=True)
    yield "The initial distance matrix is (only is known the distance to the neighbors):"
    yield latex_to_markdown(matrix_to_markdown(distance))

    for k in range(n):
        yield f"### Step {k + 1} (paths using nodes {', '.join(str(i) for i in range(k + 1))})\n"
        for i in range(n):
            for j in range(n):

                if distance[i][k] + distance[k][j] < distance[i][j]:
                    yield f"The distance between {i} and {j} has been updated as the path " \
                          f"{i} -> {k} -> {j} is shorter than the current best path {i} -> {j}\n"
                    distance[i][j] = distance[i][k] + distance[k][j]

        yield f"The distance matrix after step {k + 1} is:\n"
        yield latex_to_markdown(matrix_to_markdown(distance))

    yield "### Final result\n"
    yield f"The final distance matrix is:\n"
    yield latex_to_markdown(matrix_to_markdown(distance))
