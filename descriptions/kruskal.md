Kruskal's algorithm is a method for finding the minimum spanning tree in a graph. A minimum spanning tree is a subset of the edges of a connected, undirected graph that connects all the vertices together, without any cycles and with the minimum total edge weight.

One way to implement Kruskal's algorithm is to use a data structure called a disjoint set union (DSU). A DSU is a data structure that keeps track of a partition of a set into disjoint (non-overlapping) subsets. It has the following operations:

- makeSet(x): creates a new set with a single element x.
- findSet(x): returns the representative element of the set that contains x.
- union(x, y): merges the sets that contain x and y into a single set.

Here's how Kruskal's algorithm works using a DSU:

1. Sort the edges of the graph by weight, in ascending order.
2. Initialize a DSU with a set for each vertex in the graph.
3. For each edge in the sorted list of edges:
    - Let x and y be the two vertices of the edge.
    - If the sets that contain x and y are different (i.e., they are not already connected), as determined by the DSU's
      findSet function:
        - Add the edge to the minimum spanning tree
        - Union the two sets containing x and y using the DSU's union function.

4. Repeat steps 3 until all the vertices are connected in a single set, or until there are no more edges to consider.
   Kruskal's algorithm is a greedy algorithm, meaning that it makes the locally optimal choice at each step in the hope
   of finding a global optimum. In this case, the locally optimal choice is to always add the smallest weight edge that
   connects two disconnected vertices. The hope is that this will lead to a minimum spanning tree.

Using a DSU to implement Kruskal's algorithm allows it to run in time O(E + V log V), where E is the number of edges and
V the number of nodes in the graph. It is generally faster than the other popular algorithm for finding minimum spanning
trees, Prim's algorithm, which runs in time O(E log V), where V is the number of vertices in the graph.

First, $n$ and $m$ are given in the first line, where $n$ is the number of vertices and $m$ is the number of edges.
Then, $m$ lines follow, each containing three integers $u$, $v$ and $w$, where $u$ and $v$ are the vertices connected by
the edge and $w$ is the weight of the edge. Also, all nodes must be connected. That means that there must be a path
between any two nodes.