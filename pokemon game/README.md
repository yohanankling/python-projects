# Directed Weighted Graph - Pokemon Capture

https://user-images.githubusercontent.com/93263233/223752161-b35d25bf-a457-45e7-9059-fc2bc73d0b63.mp4


https://docs.google.com/document/d/1LrXIX2pLvRIVHdSqVIimCCxL7UBMaogAcLKfr2dOjHk/edit

This project focuses on implementing a code to create and analyze a directed weighted graph based on data from a server. The graph represents a game scenario involving agents and Pokémon, with the goal of finding the most efficient way for each agent to capture as many Pokémon as possible.

## Main Classes and Their Functions:

1. DiGraph

   The DiGraph class represents a directed graph and provides the following functions:

   - `getNode(id)`: Returns a dictionary representing the node with the given ID.
   - `getEdge(src, dest)`: Returns a dictionary representing the edge between the source and destination nodes.
   - `addPokemon(pokemon)`: Adds a Pokémon to the list of active Pokémon provided by the server. It also calculates the edge the Pokémon is on using a line formula (Y = MX + N).
   - `addAgent(agent)`: Adds an agent to the list of active agents provided by the server.
   - `v_size()`: Returns the number of nodes in the graph.
   - `e_size()`: Returns the number of edges in the graph.
   - `removePokemon(pokemon_id)`: Removes a captured Pokémon from the graph.
   - `get_all_v()`: Returns a dictionary representing all nodes in the graph.
   - `all_in_edges_of_node(id)`: Returns a dictionary representing nodes that have edges coming into the specified node.
   - `all_out_edges_of_node(id)`: Returns a dictionary representing nodes that have edges going out from the specified node.
   - `get_mc()`: Returns the number of changes made to the graph.
   - `add_edge(id1, id2, weight)`: Adds an edge between two nodes with the given weight if they exist and if an edge between them does not already exist.
   - `add_node(node_id, pos)`: Adds a new node with the given ID and position if the node does not already exist.
   - `remove_node(node_id)`: Removes a node and its associated edges from the graph if it exists.
   - `remove_edge(id1, id2)`: Removes an edge between two nodes if it exists.

2. GraphAlgo

   The GraphAlgo class provides various algorithms related to the graph and offers the following functions:

   - `get_graph()`: Returns the graph object being used.
   - `load_graph_from_json(file_name)`: Loads a graph from a JSON file.
   - `shortest_path(src, dest)`: Finds the shortest path from a source node to a destination node, returning the path as a list of nodes.
   - `dijkstra(src)`: Calculates the shortest path to all other nodes from a given source node.
   - `load_pokemons_from_json(file_name)`: Loads Pokémon data from a JSON file.
   - `load_agents_from_json(file_name)`: Loads agent data from a JSON file.
   - `center_point()`: Finds the center node of the graph, which is the node closest to all other nodes.
   - `allocate_agent(agent_id, pokemon_id)`: Allocates an agent to move toward a specified Pokémon.

3. GUI

   The GUI class represents a graphical program that displays the graph and demonstrates the Pokémon chase. It includes the following functions:

   - `drawNodes()`: Draws the nodes of the graph.
   - `drawEdges()`: Draws the edges of the graph.
   - `findMin()`: Finds the minimum coordinate values of the nodes to set the graph's drawing position.
   - `scale(scale_factor)`: Scales the graph for drawing.
   - `scaleX(scale_factor)`: Scales the graph horizontally for drawing.
   - `scaleY(scale_factor)`: Scales the graph vertically for drawing.
   - `drawPokemon(pokemon_id)`: Draws a Pokémon on the graph.
   - `drawAgent(agent_id)`: Draws an agent on the graph.

## Features of Our Algorithm:

- Read graphs from JSON files.
- Find the shortest path from a source node to a destination node.
- Display the shortest path, including the nodes on the path.
- Calculate the center of the graph, the node closest to all other nodes.
- Show the graph in a GUI window and demonstrate the agents' pursuit of Pokémon.
- Use Dijkstra's Algorithm to find the shortest paths.

## Running the Code:

1. Download the project, which includes JSON files representing various graphs.
2. Run the jar file in the command prompt (cmd) with a case number (0 to 15) to choose a specific graph and set of agents and Pokémon.
   Command: `java -jar src/Ex4_Server_v0.0.jar 0`
3. Open the project and run "main.py" to start the program.
4. Enjoy the interactive display and watch the agents chase Pokémon.

## Testing:

We have implemented several tests for the project's classes to ensure their correct functionality. All graph methods have been tested with different cases to verify their accuracy. You can also observe the agents' decisions and performance in real-time using the GUI.

## GUI:

The GUI provides a graphical representation of the graph and visualizes the agents' pursuit of Pokémon. It displays game details such as time, moves, and score. Additionally, it includes a stop button to pause the game at any level.

## Interface with the Server:

The client class facilitates communication with the server and provides essential functions to obtain the necessary data for the game's display. These functions include retrieving the graph, agents, Pokémon, starting and stopping the game, obtaining game information, moving agents, and setting agents' new destination nodes.

Enjoy playing the Pokémon Capture game and exploring the graph algorithms!
