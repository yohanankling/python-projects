import unittest
from GraphAlgo import GraphAlgo
from DiGraph import DiGraph


class MyTestCase(unittest.TestCase):

    def test_load_from_json(self):
        g = GraphAlgo()
        GraphAlgo.load_from_json(g, "../data/A0.json")
        graph1 = g.get_graph()
        nodesize = graph1.v_size()
        self.assertEqual(nodesize, 11)
        edgesize = graph1.e_size()
        self.assertEqual(edgesize, 22)

    def test_save_to_json(self):
        pass

    def test_shortest_path(self):
        g_algo = GraphAlgo()
        file = "../data/T0.json"
        g_algo.load_from_json(file)
        dist, path = g_algo.shortest_path(0, 3)
        self.assertEqual(dist, 2.8)
        self.assertEqual(path, [0, 1, 3])
        dist, path = g_algo.shortest_path(3, 1)
        self.assertEqual(dist, float('inf'))
        self.assertEqual(path, [])
        dist, path = g_algo.shortest_path(335531, 1)
        self.assertEqual(dist, float('inf'))
        self.assertEqual(path, [])

    def test_centerPoint(self):
        graph = DiGraph()
        g = GraphAlgo(graph)
        GraphAlgo.load_from_json(g, "../data/A0.json")
        center = g.centerPoint()
        self.assertEqual(center[0], 7)
        self.assertEqual(center[1], 6.806805834715163)

    def test_get_graph(self):
        graph = DiGraph()
        graph.add_node(0)
        graph.add_node(1)
        graph.add_node(2)
        graph.add_node(2)
        tup = (35.0, 32.1, 0.0)
        graph.add_node(3, tup)
        graph.add_edge(0, 1, 1)
        graph.add_edge(0, 2, 1)
        graph.add_edge(0, 1, 2)
        graph.add_edge(0, 3, 1)
        nodesize = graph.v_size()
        self.assertEqual(nodesize, 4)
        edgesize = graph.e_size()
        self.assertEqual(edgesize, 3)


if __name__ == '__main__':
    unittest.main()
