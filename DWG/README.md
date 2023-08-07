# oop_Ex3 - Directed Weighted Graph
https://docs.google.com/document/d/15sTWy_pa6Vg4r7phAC322vZA169V02yezjxxf4b9sJc/edit

## Introduction
This project focuses on the implementation of a directed weighted graph, along with various graph algorithms and a graphical user interface (GUI) to visualize and interact with the graphs. The main goal is to read graphs from JSON files, perform various operations on the graphs, and save the results efficiently.

## Classes and Functions

### DiGraph
- `getNode(id)`: Get the node with the given ID and return its information as a dictionary.
- `getEdge(src, dest)`: Get the edge between the source node and destination node and return its information as a dictionary.
- `v_size()`: Return the number of nodes in the graph.
- `e_size()`: Return the number of edges in the graph.
- `get_all_v()`: Return a dictionary containing all nodes in the graph.
- `all_in_edges_of_node(id)`: Get the nodes that have edges entering the specified node and return them as a dictionary.
- `all_out_edges_of_node(id)`: Get the nodes that have edges leaving the specified node and return them as a dictionary.
- `get_mc()`: Return the number of changes made to the graph.
- `add_edge(id1, id2, weight)`: Add an edge between nodes with IDs id1 and id2 with the given weight. Return true if the operation is successful, false otherwise.
- `add_node(node_id, pos)`: Add a node with the given ID and position to the graph. Return true if the operation is successful, false if the node already exists.
- `remove_node(node_id)`: Remove the node with the given ID from the graph, along with its incident edges. Return true if the operation is successful, false otherwise.
- `remove_edge(node_id1, node_id2)`: Remove the edge between nodes with IDs node_id1 and node_id2. Return true if the operation is successful, false if the edge does not exist.

### GraphAlgo
- `get_graph()`: Get the underlying directed weighted graph.
- `load_from_json(file_name)`: Load a graph from a JSON file with the given file_name.
- `save_to_json(file_name)`: Save the graph to a JSON file with the given file_name.
- `shortest_path(src, dest)`: Find the shortest path from the source node to the destination node using Dijkstra's algorithm. Return a list of nodes representing the shortest path.
- `dijkstra(src)`: Compute the shortest path from the source node to all other nodes in the graph using Dijkstra's algorithm. Return a dictionary with the shortest path distances.
- `isPathConnected()`: Check if there is a valid path connecting all nodes in the graph. Return true if there is a valid path, false otherwise.
- `isConnected()`: Check if the graph is strongly connected, meaning there is a path between any two nodes in both directions. Return true if the graph is strongly connected, false otherwise.
- `TSP(targets)`: Compute the Traveling Salesman Problem (TSP) solution for a list of target nodes. Return a list of nodes representing the shortest TSP path.
- `centerPoint()`: Calculate the center point of the graph, which is the node closest to all other nodes in terms of the sum of shortest path distances.
- `plot_graph()`: Visualize the graph using a graphical interface.

### GUI
- `drawNodes()`: Draw the nodes of the graph on the GUI.
- `drawEdges()`: Draw the edges of the graph on the GUI.
- `findMin()`: Find the minimum value among a given set of nodes.
- `scale(scale_factor)`: Scale the graph on the GUI by a given factor.
- `scaleX(scale_factor)`: Scale the graph horizontally on the GUI by a given factor.
- `scaleY(scale_factor)`: Scale the graph vertically on the GUI by a given factor.

## Features
- Read graphs from JSON files and perform various operations on them.
- Find the shortest path between two nodes using Dijkstra's algorithm.
- Save the graph after performing calculations to optimize efficiency.
- Check if the graph is path-connected and strongly connected.
- Calculate the Traveling Salesman Problem (TSP) solution for a list of target nodes.
- Determine the center point of the graph, which is the node closest to all other nodes.
- Visualize the graph using a user-friendly graphical interface.

## How to Run
1. Download the project and navigate to the main class.
2. Ensure you have the required JSON files representing graphs. You can also add your custom JSON files in the same format.
3. Run the main class, and you will see the default graph A0. You can load other graphs using the `load_from_json` function in `GraphAlgo`.
4. Use or explore the implemented tests on the classes within the project.

## GUI
The GUI provides a graphical representation of the graph, allowing you to interact with it visually. You can view nodes and edges, find minimum values, and scale the graph to your preference.

We used Dijkstra's algorithm for finding the shortest path in this implementation.

Feel free to explore, use, and modify the code as needed for your projects. Enjoy visualizing and working with graphs effortlessly!
