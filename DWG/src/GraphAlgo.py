import json
import random
from queue import PriorityQueue
from typing import List

from GraphAlgoInterface import GraphAlgoInterface
from src.DiGraph import DiGraph
from src.GraphInterface import GraphInterface
from src.GUI import GUI



class GraphAlgo (GraphAlgoInterface):
    def __init__(self, graph = None):
        if graph == None:
            graph = DiGraph()
        self.graph: DiGraph = graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        myGraph = DiGraph()
        try:
            json_file = open(file_name)
            graph = json.load(json_file)
            json_file.close()
            nodes = graph["Nodes"]
            for i in range(len(nodes)):
                id = nodes[i]["id"]
                tup = (random.uniform(35.19, 35.20), random.uniform(32.09, 32.109))
                try:
                    pos = nodes[i]["pos"]
                    tup = pos.split(',')
                except:
                    pass
                myGraph.add_node(id, tup)
            edges = graph["Edges"]
            for i in range(len(edges)):
                src = edges[i]["src"]
                dest = edges[i]["dest"]
                weight = edges[i]["w"]
                myGraph.add_edge(src, dest, weight)
            self.__init__(myGraph)
        except:
            print("oups!")
            return False
        return True


    def save_to_json(self, file_name: str) -> bool:
        dict = {"Edges": [], "Nodes": []}
        for i in self.graph.edges:
            dict["Edges"].append({"src": i[0], "w": self.graph.edges[i[0], i[1]], "dest": i[1]})
        for i in self.graph.nodes:
            dict["Nodes"].append({"pos": self.graph.nodes[i], "id": i})
        try:
            with open(file_name, 'w') as f:
                 json.dump(dict, indent=2, fp=f)
        except:
            return False
        return True

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        ans = self.isPathConnected(id1, id2)
        if not ans:
            return float('inf'), []
        d, allPath = self.dijkstra(id1)
        i = id2
        path = []
        path.append(id2)
        while i != id1:
            path.append(allPath[i])
            i = allPath[i]
        path.reverse()
        return d[id2], path

    def dijkstra(self, src) -> (list, list):
        if src not in self.graph.nodes:
            return None
        path = {v: -1 for v in self.graph.nodes}
        visited = {v: False for v in self.graph.nodes}
        dist = {}
        for i in range(len(self.graph.nodes)):
            if src is not i:
                if self.graph.getEdge(src, i):
                    dist[i] = self.graph.edges[src, i]
                else:
                    dist[i] = float('inf')
            else:
                dist[i] = 0
        weight = {v: -1 for v in self.graph.nodes}
        weight[src] = 0
        pq = PriorityQueue()
        pq.put((0, src))
        while not pq.empty():
            (distance, current_vertex) = pq.get()
            visited[current_vertex] = True
            for neighbor in self.graph.all_out_edges_of_node(current_vertex):
                weight = self.graph.edges[current_vertex, neighbor]
                if not visited[neighbor]:
                    oldCost = dist[neighbor]
                    newCost = dist[current_vertex] + weight
                    if newCost <= oldCost:
                        dist[neighbor] = newCost
                        path[neighbor] = current_vertex
                        pq.put((newCost, neighbor))
        return dist, path

    def isPathConnected(self, src, dest):
        if dest not in self.graph.nodes:
            return None
        if src not in self.graph.nodes:
            return None
        ans = True
        dist, path = self.dijkstra(src)
        if dist[dest] == float('inf'):
                ans = False
        return ans

    def isConnected(self):
        ans = True
        for i in self.graph.nodes:
            dist, path = self.dijkstra(i)
            for i in dist.values():
                if i == float('inf'):
                    ans = False
        return ans

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        ans = []
        ans.append(node_lst[0])
        min = {v: v for v in node_lst}
        for all in node_lst:
            visited = {v: False for v in node_lst}
            counter = all
            sum = 0
            for i in node_lst:
                distances = {v: 0 for v in node_lst}
                for j in node_lst:
                    dist, path = self.shortest_path(node_lst[counter], node_lst[j])
                    distances[j] = dist
                sortDistances = sorted(distances.items(), key=lambda x: x[1])
                visited[i] = True
                for k in node_lst:
                    if sortDistances[k][1] != 0 and not visited[sortDistances[k][0]]:
                        counter = k
                        sum = sum + sortDistances[k][1]
                        ans.append(k)
                        break
            min[all] = sum
        dis = sorted(min.items(), key=lambda x: x[1])
        return ans, dis

    def centerPoint(self) -> (int, float):
        counter = -1
        max = 0
        min = float('inf')
        for src in range(len(self.graph.nodes)):
            dist = self.dijkstra(src)
            max = 0
            for i in dist[0]:
                if dist[0][i] > max:
                    max = dist[0][i]
            if min > max:
                min = max
                counter = src
        return counter, min

    def plot_graph(self) -> None:
        GUI(self.get_graph())
        pass

    def __repr__(self):
        return self.graph.__repr__()