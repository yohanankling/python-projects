from src import DiGraph


class Pokemon:
    def __init__(self, value: float, type: int, graph: DiGraph, tup: ()) -> None:
        self.value: float = value
        self.type: int = type
        self.pos: () = tup.split(',')
        self.edge: tup = ()
        self.edge = self.getEdge(graph, self.pos)
        self.care: int = -1
        self.first: bool = False

    def getEdge(self, graph: DiGraph, pos: ()):
        for edge in graph.edges:
            src = graph.getNode(edge[0])
            m = graph.getEdge(edge[0], edge[1])[1]
            line = (m*float(src[0]) - float(src[1]))*(-1)
            res = abs(float(pos[1]) - (float(pos[0]) * m + line))
            if res < 0.00000000001:
                if self.type > 0:
                    return min(edge[0], edge[1]), max(edge[0], edge[1])
                else:
                    return max(edge[0], edge[1]), min(edge[0], edge[1])

    def setCare(self, care: str):
        self.care = int(care)

    def setFirst(self, care: bool):
        self.first = care

    def __repr__(self):
        return "Pokemon:" + " value:" + self.value.__repr__() + ",type" + self.type.__repr__() + ",pos" + self.pos.__repr__() + ",care" +self.care.__repr__() + ",first" +self.first.__repr__()
