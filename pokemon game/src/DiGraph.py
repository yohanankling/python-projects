import random

from GraphInterface import GraphInterface
from Pokemon import Pokemon
from Agent import Agent


class DiGraph(GraphInterface):
    def __init__(self, nodes: {}, edges: {}, pokemons: {}, agents: {}) -> None:
        self.nodes: {} = nodes
        self.edges: {} = edges
        self.pokemons: {} = pokemons
        self.agents: {} = agents

    def __init__(self) -> None:
        self.nodes: {} = {}
        self.edges: {} = {}
        self.pokemons: {} = {}
        self.agents: {} = {}

    def getNode(self, id):
        if id not in self.nodes.keys():
            return False
        return self.nodes[id]

    def getEdge(self, src, dest):
        try:
            return self.edges[src, dest]
        except:
            return False

    def getPokemons(self):
        return self.pokemons

    def getAgents(self):
        return self.agents

    def v_size(self) -> int:
        return len(self.nodes)

    def e_size(self) -> int:
        return len(self.edges)

    def p_size(self) -> int:
        return len(self.pokemons)

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

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 not in self.nodes.keys() or id2 not in self.nodes.keys():
            return False
        if self.getEdge(id1, id2):
            return False
        src = self.getNode(id1)
        dest = self.getNode(id2)
        m = (float(src[1]) - float(dest[1])) / (float(src[0]) - float(dest[0]))
        self.edges[id1, id2] = weight, m
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.nodes.keys():
            return False
        if pos == None:
            pos = (random.uniform(35.19, 35.20), random.uniform(32.09, 32.109))
        self.nodes[node_id] = pos
        return True

    def add_pokemon(self, pokemon: Pokemon) -> bool:
        pokemonsToRemove = []
        for p in self.pokemons:
            if p.pos[0] == pokemon.pos[0] and p.pos[1] == pokemon.pos[1]:
                return False
        for p in self.pokemons:
            if p.first == False:
                pokemonsToRemove.append(p)
        self.remove_pokemon(pokemonsToRemove)
        self.pokemons[pokemon] = pokemon
        return True

    def add_agent(self, agent: Agent) -> bool:
        self.agents[agent.id] = agent
        return True

    def remove_pokemon(self, pokemon: []):
        for i in range(len(pokemon)):
            del self.pokemons[pokemon[i]]

    def __repr__(self):
        return "Nodes: " + self.nodes.__repr__() + " Edges: " + self.edges.__repr__() + " Pokemons: " + self.pokemons.__repr__()
