Prim's algorithm is an algorithm for finding a minimum spanning tree for a weighted undirected graph. A minimum spanning tree is a subset of the edges of a graph that forms a tree and connects all the vertices, without any cycles and with the minimum total edge weight.

Here's how the algorithm works:

1. Start with a vertex and include all its incident edges (edges that connect to the vertex) in a priority queue (a
   queue where elements are ordered according to a priority).

2. Repeat the following steps until all vertices are included in the tree:
   - Select the edge with the minimum weight from the queue. If the edge connects a vertex already in the tree to a
     vertex not in the tree, add the vertex to the tree and include all its incident edges in the queue. If the edge
     connects two vertices already in the tree, discard the edge.

3. The resulting tree is the minimum spanning tree.

The complexity of the best implementation of Prim's algorithm is O(E log E), where E is the number of edges and V is the
number of vertices in the graph. This means that the algorithm's running time increases logarithmically with the number
of vertices and linearly with the number of edges.

In summary, Prim's algorithm is a simple and efficient way to find the minimum spanning tree for a weighted undirected
graph.

The input must be a graph in the following format:

First, $n$ and $m$ are given in the first line, where $n$ is the number of vertices and $m$ is the number of edges.
Then, $m$ lines follow, each containing three integers $u$, $v$ and $w$, where $u$ and $v$ are the vertices connected by
the edge and $w$ is the weight of the edge. Also, all nodes must be connected. That means that there must be a path
between any two nodes.
