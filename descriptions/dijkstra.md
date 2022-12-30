Dijkstra's algorithm is an algorithm for finding the shortest path between two nodes in a graph. It is a popular
algorithm for finding the shortest path because it is relatively efficient and easy to implement.

The basic idea behind Dijkstra's algorithm is to explore the graph starting from the source node, and to keep track of
the shortest distance from the source node to each other node in the graph. To do this, we use a priority queue, which
is a data structure that allows us to efficiently find the next node to explore based on its distance from the source.

Here is a simple version of Dijkstra's algorithm using a priority queue:

1. Initialize a priority queue and a distance table, where the distance table keeps track of the shortest distance from
   the source node to each other node in the graph.
2. Add the source node to the priority queue with a distance of 0.
3. While the priority queue is not empty:
    - Pop the node with the smallest distance from the priority queue.
    - For each of the node's neighbors:
        - Calculate the distance to the neighbor by adding the distance from the source to the node to the weight of the
          edge between the node and the neighbor.
        - If the calculated distance is less than the current distance in the distance table, update the distance table
          with the new distance and add the neighbor to the priority queue.

4. When the priority queue is empty, the distance table will contain the shortest distances from the source node to
   every other node in the graph.

Dijkstra's algorithm is often used to find the shortest path between two nodes in a graph, but it can also be used to
find the shortest path between a single source node and all other nodes in the graph.

First, $n$, $m$ and $u$ are given in the first line, where $n$ is the number of vertices, $m$ is the number of edges and
$u$ the source node (must be in the range $[0,n-1]$).
Then, $m$ lines follow, each containing three integers $u$, $v$ and $w$, where $u$ and $v$ are the vertices connected by
the edge and $w$ is the weight of the edge.

In the last line, $s$ is given, where $s$ is the source node (must be in the range $[0,n-1]$).
