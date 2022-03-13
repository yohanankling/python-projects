# oop_Ex4
# Assignment of oop_Ex4
https://docs.google.com/document/d/1LrXIX2pLvRIVHdSqVIimCCxL7UBMaogAcLKfr2dOjHk/edit

Directed Weighted Graph - pokemon capture
In this project we wrote a code for getting graph from  server, agents and pokemons and calculate the most efficiant way for every agent to the pokemons as the goal - is to capture as most pokemons as possible.


# The main classes and their function:
- DiGraph

  DiGraph represents a graph with some functions:
  * getNode - gets "id" and returns dict of its node
  * getEdge - gets "src, dest" and returns dict of its edge
  * addPokemon - adding pokemon to the actual pokemons list that the server provided, deleting the older list with non actual pokemons
  the class Pokemon claculate also the edge the pokemon on with the line formula - Y=XM + N
  * addAgent - adding agent to the actual agents list that the server provided
  * v_size - returns the length of nodes's dict
  * e_size - returns the length of edges's dict
  * removePokemon - removing captured pokemons
  * get_all_v - return the nodes's dict
  * all_in_edges_of_node - gets "id1" and returns dict of nodes which enter to this node  
  * all_out_edges_of_node - gets "id1" and returns dict of nodes which go out from this node
  * get_mc -  returns num of changes in graph
  * add_edge -  gets "id1, id2, waight" and returns false if node of id1 or node of id2 does not         exsist and return true and add this edge if they exsist and there is not edge between them
  * add_node - gets "node_id, pos" and returns false if node_id is exsist and return true and add         this node if node_id is not exsist
  * remove_node - gets "node_id and returns false if node_id does not exsist and return true and         delete this node and its edges if it exsist 
  * remove_edge - gets "node_id, node_id" and returns false if node_id1 or node_id2 or this edge does     not exsist and return true and delete this edge if they are exsist
  
on this way We will present the following two classes.

- GraphAlgo

  GraphAlgo represents some algorithms  of the graph with some functions:
  * get_graph 
  * load_graph_from_json 
  * shortest_path 
  * dijkstra
  * load_pokemons_from_json 
  * load_agents_from_json 
  * centerPoint 
  * allocateAgent

- GUI

  GUI represents graphic program ,that show you the graph and demonstrate it, with some functions:
  * drawNodes 
  * drawEdges 
  * findMin 
  * scale 
  * scaleX 
  * scaleY
  * drawPokemon
  * drawAgent
 
# Features of our algorithm :
Reading graphs from json file.
Checking what is the shortest path from source node to destination node.
Giving the shortest path from src node to dest node (with nodes which in the 'road').
Calculation the center of the graph (the most close node to the all other nodes).
Showing the graph in gui window - and demonstrate the chasing for the pokemons
In this code we used Dijkstra Algorithm to get the shortest path.
the main propose is to loacate the closet pokemon to an agent and to send him there.

# Code's running:
For run the code you can download the project. Then, you will find: some json files, representing the graphs, you need to run the jar file in the cmd with the wanted case that representing diffrent grpah or agnets and pokemons, and run the "main" file in the project.
runing levels:
- run the command(make sure you oppened the cmd in the same folder the jar there) - 
"java -jar src/Ex4_Server_v0.0.jar 0" (0 = case 0, you can go from 0 to 15)
- open the project and run "main.py"
- enjoy

# Test:
we implemented some tests on our classes in the project.
all graph method checked with some casses to test them.
also, we can see the actual decision the program take in a live in the gui and the agnets work in a good way.


# Gui:
You can use graphic program that show you the graph and demonstrate it, and see the agnets in their chase after pokemons,
you can see in the left corner the game details- time,moves and score as an stop button to stop the game in any level you want

# interface with the server :
the client class have some function to help us get the details neccesary to the game to display the pokemon chase -
getGraph, getAgnets, getPokemons, start(to start the gmae), stop, info (of the game), move (to reset agnets pos), nextEdge (set the agent his new destination node to go there - only for his neibher)

# enjoy.
