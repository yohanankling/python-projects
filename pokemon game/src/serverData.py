from client import Client
PORT = 6666
HOST = '127.0.0.1'

class serverData:
    def __init__(self) -> None:
        self.client = Client()
        self.client.start_connection(HOST, PORT)

    def getGraph(self):
        graph_json = self.client.get_graph()
        return graph_json

    def getPokemons(self):
        graph_json = self.client.get_pokemons()
        return graph_json

    def addAgent(self, place: int):
        self.client.add_agent("{\"id\":%d}" % place)

    def startGame(self):
        self.client.start()

    def getTime(self):
        if not self.isOnline():
            return ''
        return self.client.time_to_end()

    def isOnline(self):
        try:
            if self.client.is_running() != 'true':
                return 'False'
        except:
            return False
        return self.client.is_running()

    def getAgents(self):
        if not self.isOnline():
            return ''
        return self.client.get_agents()

    def stopGame(self):
        self.client.stop_connection()

    def getInfo(self):
        if not self.isOnline():
            return ''
        return self.client.get_info()

    def getTime(self):
        if not self.isOnline():
            return ''
        return self.client.time_to_end()

    def setNextEdge(self, agentId, edge):
        if not self.isOnline():
            return ''
        self.client.choose_next_edge(
            '{"agent_id":' + str(agentId) + ', "next_node_id":' + edge + '}')

    def move(self):
        if not self.isOnline():
            return ''
        self.client.move()