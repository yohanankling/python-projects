import random

from GraphInterface import GraphInterface

class DiGraph(GraphInterface):
    def __init__(self, nodes: {}, edges: {}) -> None:
        self.nodes: {} = nodes
        self.edges: {} = edges
        self.mc = 0

    def __init__(self) -> None:
        self.nodes: {} = {}
        self.edges: {} = {}
        self.mc = 0

    def getNode(self, id):
        if id not in self.nodes.keys():
            return False
        return self.nodes[id]

    def getEdge(self, src, dest):
        try:
            return self.edges[src, dest]
        except:
            return False


    def v_size(self) -> int:
        return len(self.nodes)

    def e_size(self) -> int:
        return len(self.edges)

    def get_all_v(self) -> dict:
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        nodesIn = {}
        for k in self.edges.keys():
            if k[1] == id1:
                 nodesIn[k[0]] = [k[0], self.edges[k[0], id1]]
        return nodesIn

    def all_out_edges_of_node(self, id1: int) -> dict:
        nodesOut = {}
        for k in self.edges.keys():
            if k[0] == id1:
                nodesOut[k[1]] = [k[1], self.edges[id1, k[1]]]
        return nodesOut

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 not in self.nodes.keys() or id2 not in self.nodes.keys():
            return False
        if self.getEdge(id1, id2):
            return False
        self.mc = self.mc + 1
        self.edges[id1, id2] = weight
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.nodes.keys():
            return False
        self.mc = self.mc + 1
        if pos == None:
            pos = (random.uniform(35.19, 35.20), random.uniform(32.09, 32.109))
        self.nodes[node_id] = pos
        return True

    def remove_node(self, node_id: int) -> bool:
        if self.getNode(node_id):
            dictIn = self.all_in_edges_of_node(node_id)
            while (len(dictIn)>0):
                self.remove_edge(dictIn.popitem()[0], node_id)
            dictOut = self.all_out_edges_of_node(node_id)
            while (len(dictOut)>0):
                self.remove_edge(node_id, dictOut.popitem()[0])
            self.mc = self.mc + 1
            del self.nodes[node_id]
            return True
        else:
            return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if self.getEdge(node_id1, node_id2):
            self.mc = self.mc + 1
            del self.edges[node_id1, node_id2]
            return True
        else:
            return False


    def __repr__(self):
        return "Nodes: " + self.nodes.__repr__() + " Edges: " + self.edges.__repr__()