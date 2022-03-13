import json
import random
from queue import PriorityQueue

from GraphAlgoInterface import GraphAlgoInterface
from src.Agent import Agent
from src.DiGraph import DiGraph
from src.GraphInterface import GraphInterface
from Pokemon import Pokemon

class GraphAlgo (GraphAlgoInterface):
    def __init__(self, graph = None):
        if graph == None:
            graph = DiGraph()
        self.graph: DiGraph = graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_graph_from_json(self, graph_json: str) -> bool:
        myGraph = DiGraph()
        graph_json = json.loads(graph_json)
        nodes = graph_json["Nodes"]
        for node in nodes:
            id = node["id"]
            tup = (random.uniform(35.19, 35.20), random.uniform(32.09, 32.109))
            try:
                pos = node["pos"]
                tup = pos.split(',')
            except:
                pass
            myGraph.add_node(id, tup)
        edges = graph_json["Edges"]
        for edge in edges:
            src = edge["src"]
            dest = edge["dest"]
            weight = edge["w"]
            myGraph.add_edge(src, dest, weight)
        self.__init__(myGraph)

    def load_agents_from_json(self, agent_json: str):
        graph = self.get_graph()
        agent_json = json.loads(agent_json)
        agents = agent_json["Agents"]
        for agent in agents:
            id = (agent["Agent"]["id"])
            value = (agent["Agent"]["value"])
            src = (agent["Agent"]["src"])
            dest = (agent["Agent"]["dest"])
            speed = (agent["Agent"]["speed"])
            pos = (random.uniform(35.19, 35.20), random.uniform(32.09, 32.109))
            try:
                pos = (agent["Agent"]["pos"])
            except:
                pass
            agent = Agent(id, value, src, dest, speed, pos)
            graph.add_agent(agent)
        self.__init__(graph)

    def load_pokemons_from_json(self, pokemon_json: str):
        graph = self.get_graph()
        pokemon_json = json.loads(pokemon_json)
        pokemons = pokemon_json["Pokemons"]
        for pokemon in pokemons:
            value = (pokemon["Pokemon"]["value"])
            type = (pokemon["Pokemon"]["type"])
            pos = (random.uniform(35.19, 35.20), random.uniform(32.09, 32.109))
            try:
                pos = (pokemon["Pokemon"]["pos"])
            except:
                pass
            pokemon = Pokemon(value, type, self.get_graph(), pos)
            pokemon.setFirst(True)
            graph.add_pokemon(pokemon)
        self.__init__(graph)

    def shortest_path(self, id1: int, id2: int) -> (float, list):
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
                    dist[i] = self.graph.edges[src, i][0]
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
                weight = self.graph.edges[current_vertex, neighbor][0]
                if not visited[neighbor]:
                    oldCost = dist[neighbor]
                    newCost = dist[current_vertex] + weight
                    if newCost <= oldCost:
                        dist[neighbor] = newCost
                        path[neighbor] = current_vertex
                        pq.put((newCost, neighbor))
        return dist, path

    def centerPoint(self) -> (int, float):
        counter = -1
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

    def allocate_agent(self, agent):
        graph = self.get_graph()
        speed = float(agent.speed)
        minDist = float('inf')
        dist = -1
        for pokemon in graph.pokemons:
            if pokemon.care != agent.id:
                if pokemon.care != -1:
                    continue
            min_edge = min(pokemon.edge)
            max_edge = max(pokemon.edge)
            if pokemon.type > 0:
                dist, path = self.shortest_path(agent.src, min_edge)
                dist = float(dist) / speed
            else:
                dist, path = self.shortest_path(agent.src, max_edge)
                dist = float(dist) / speed
            if float(dist) < minDist:
                minDist = dist
                minPath = path
                pos = pokemon.pos
        if dist == -1:
            return dist, None, None
        for checkP in graph.pokemons:
            if pos == checkP.pos:
                checkP.setCare(agent.id)
                pokemon = checkP
        return minDist, minPath, pokemon

    def distance_agent(self, agent, nodeId):
        agentPos = agent.pos
        agentPos = agentPos.split(',')
        node = self.graph.nodes[int(nodeId)]
        x = (abs(float(agentPos[0]) - float(node[0])))**2
        y = (abs(float(agentPos[1]) - float(node[1])))**2
        distance = (x + y) ** 0.5
        distance = distance / agent.speed
        return distance

    def getMin(self):
        graph = self.get_graph()
        dict = graph.get_all_v()
        maxX = float('-inf')
        maxY = float('-inf')
        minX = float('inf')
        minY = float('inf')
        for n in dict.values():
            if float(n[0]) > maxX:
                maxX = float(n[0])
            if float(n[1]) > maxY:
                maxY = float(n[1])
            if float(n[0]) < minX:
                minX = float(n[0])
            if float(n[1]) < minY:
                minY = float(n[1])
        return minX, maxX, minY, maxY

    def __repr__(self):
        return self.graph.__repr__()