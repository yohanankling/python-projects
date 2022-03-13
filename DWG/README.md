# oop_Ex3
# Assignment of oop_Ex3
https://docs.google.com/document/d/15sTWy_pa6Vg4r7phAC322vZA169V02yezjxxf4b9sJc/edit

Directed Weighted Graph
In this project we wrote a code for getting graphs from json file and save them after implementing some functions.

# The main classes and their function:
- DiGraph
  DiGraph represents a graph with some functions:
  * getNode - gets "id" and returns dict of its node
  * getEdge - gets "src, dest" and returns dict of its edge
  * v_size - returns the length of nodes's dict
  * e_size - returns the length of edges's dict
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
  * load_from_json 
  * save_to_json 
  * shortest_path 
  * dijkstra
  * isPathConnected  
  * isConnected 
  * TSP       
  * centerPoint 
  * plot_graph 


- GUI
  GUI represents graphic program ,that show you the graph and demonstrate it, with some functions:
  * drawNodes 
  * drawEdges 
  * findMin 
  * scale 
  * scaleX 
  * scaleY
 
# Features of our algorithm :
Reading graphs from json file.
Checking what is the shortest path from source node to destination node.
Giving the shortest path from src node to dest node (with nodes which in the 'road').
Saving the graph after calculation it with some algorithms to make it more efficient.
Checking tsp.
Calculation the center of the graph (the most close node to the all other nodes).
Showing the graph in gui window.
In this code we used Dijkstra Algorithm to get the shortest path.

# Code's running:
For run the code you can download the project. Then, you will find: some json files, representing the graphs, you can add at yourself also in the same format.
you can run the main class and you will see the A0 graph as deafult. you can also get other graph by using the load funcion in GarphAlgo.
Test:
we implemented some tests on our classes in the project. You can use or see them as you want.

# Gui:
You can use graphic program that show you the graph and demonstrate it.

# java vs python :
on java we didnt implement in sucsess the functions that used dijakstra algorithm so we cant tell whos working better.
