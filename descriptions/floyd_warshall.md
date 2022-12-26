The Floyd–Warshall algorithm is an algorithm for finding shortest paths in a weighted graph with positive or negative
edge weights (but with no negative cycles). A single execution of the algorithm will find the lengths (summed weights)
of the shortest paths between all pairs of vertices.

The algorithm is based on the observation that the shortest path between any two vertices in a graph can be found by
considering all of the intermediate vertices that could be used to connect the two vertices. For example, if you want to
find the shortest path between vertices A and C in a graph, you could first find the shortest path between A and B, then
the shortest path between B and C, and finally add these two lengths together to get the shortest path between A and C.

The Floyd–Warshall algorithm works by iteratively improving the estimates of the shortest path between all pairs of
vertices. It does this by considering each vertex in turn and using it as an intermediate vertex to update the shortest
path between every other pair of vertices. This process is repeated for each vertex until the final shortest path
between all pairs of vertices is found.

The time complexity of the Floyd–Warshall algorithm is O(n^3), where n is the number of vertices in the graph. This
makes it suitable for use on large graphs, although other algorithms may be faster for certain types of graphs.

Overall, the Floyd–Warshall algorithm is a useful tool for finding the shortest paths between all pairs of vertices in a
graph, and is particularly useful for graphs with negative edge weights.

First, $n$ and $m$ are given in the first line, where $n$ is the number of vertices and $m$ is the number of edges.
Then, $m$ lines follow, each containing three integers $u$, $v$ and $w$, where $u$ and $v$ are the vertices connected by
the edge and $w$ is the weight of the edge.