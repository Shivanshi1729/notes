---
layout: default
title: Unit III
parent: Design and Analysis of Algorithms
mathjax: true
mermaid: true
---

# Unit III

- Graph Algorithms 
  - Representation of Graphs, 
  - Breadth-first search (BFS), 
  - depth-first search (DFS), 
  - topological sort, 
  - Difference between BFS and DFS 
- Data structures for disjoint sets 
  - Finding cycle in a graph, 
  - Finding strongly connected components 
- Minimum spanning trees
  - Kruskal and Prim algorithms (Greedy Algorithms) 
- Single source shortest paths
    - Dijkstra (Greedy Approach) and Bellman ford (Dynamic Programming) algorithms 
- All pair shortest paths 
  - The Floyd Warshall algorithm

## Graph

- What is Graph?

> in math

a pair $G = (V, E)$ where
- $V$ - set of vertices
- $E$ - set of edges

> in cs as an ADT

- set of vertices
- set of unordered pair (for undirected graph)
- set of ordered pairs (for directed graph)
- set of tuples (for weight in the graph)

### Operations on Graph

Here `G` will represent the graph, `V` vertices and `E` the edges

- `adjacent(G, x, y)`
  - tells wether there is an edge from `x` to `y` in the graph
  - `(x, y)` belongs to `E`
- `neighbors(G, x)`
  - `{y | y belongs to V and adjacent(G, x, y) is true}`
- `add_vertex(G, x)`
  - add a new element `x` to `V`
- `remove_vertex(G, x)`
  - remove element `x` from `V`
- `add_edge(G, x, y)`
  - add `(x, y)` to `E`
- `remove_edge(G, x, y)`
  - remove `(x,y)` form `E`
- `get_vertex_value(G, x)`
  - get the value associated with the vertex `x`
  - i.e. some label on the `x`
- `set_vertex_values(G, x, v)`
  - set the value associated with the vertex `x` to `v`
- `set_edge_value(G, x, y, v)`
  - set the weight for the edge `(x, y)` to `v`
- `get_edge_value(G, x, y)`
  - get the weight for the edge `(x, y)`

## Graph Representation

- adjacency list

In adjacency list all vertex are stored in an array, and each vertex have a linked list which store 
the adjacent elements.

- adjacency matrix

In this there is a matrix of dimension equal to the no of vertices, presence of edge between
x, and y is denoted by setting the value of matrix at i row and j col to 1, else it is infinite.

- incidence matrix

- Store graph
  - `O(|V|+|E|)` - list
  - `O(|V|^2)` - matrix
- Add vertex 
  - `O(1)` - list
  - `O(|V|^2)` - matrix
- Add edge
  - `O(1)` - list
  - `O(1)` - matrix
- Remove Vertex
  - `O(|E|)` - list
  - `O(|V|^2)` - matrix
- Remove edge
  - `O(|V|)` - list
  - `O(1)` - matrix
- are vertices x and y adjacent
  - `O(|V|)` - list
  - `O(1)` - matrix

## Graph algorithms

### Breadth first search

**Algorithm**

```
BFS(G, root):
    Q := queue()
    visited := []

    visited[root] := true
    Q.enqueue(root)

    while Q is not empty do:
        v := Q.dequeue()
        for all edges from v to w in G.adjacentEdges(v) do:
            if not visited[w] then:
                visited[w] = true
                Q.enqueue(w)
```

```cpp
void bfs(vector<vector<int>> graph, int start, bool *visited) {
    list<int> queue;

    // make current node visited
    visited[start] = true;
    queue.push_back(start);

    while (!queue.empty()) {
        start = queue.front();
        cout << start << "->";
        queue.pop_front();

        // get all the adjacent enqueued
        for (int i = 0; i < graph[start].size(); i++) {
            if (!visited[graph[start][i]]) {
                visited[graph[start][i]] = true;
                queue.push_back(graph[start][i]);
            }
        }
    }
}
```