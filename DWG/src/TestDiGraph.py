import unittest
from DiGraph import DiGraph

class MyTestCase(unittest.TestCase):
    graph = DiGraph()
    graph.add_node(0, (6, 5, 4))
    graph.add_node(2, (2, 5, 4))
    graph.add_node(4, (3, 6, 7))
    graph.add_node(6, (2, 2, 2))
    graph.add_edge(0, 4, 7.4)
    graph.add_edge(6, 2, 6.7)
    graph.add_edge(2, 4, 8)
    graph.add_edge(6, 0, 2.2)

    def test_v_size(self):
        self.assertEqual(len(self.graph.nodes), 4)

    def test_e_size(self):
        self.assertEqual(len(self.graph.edges), 4)

    def test_get_mc(self):
        self.assertEqual(self.graph.mc, 8) # 4 add_node and 4 add_edge

    def test_get_all_v(self):
        nodes = {0: (6, 5, 4), 2: (2, 5, 4), 4: (3, 6, 7), 6: (2, 2, 2)}
        nodesG =self.graph.get_all_v()
        self.assertDictEqual(nodesG, nodes)

    def test_all_in_edges_of_node(self):
        allIn = self.graph.all_in_edges_of_node(0)
        inNodes = {6: [6, 2.2]}
        self.assertDictEqual(allIn, inNodes)

    def test_out_in_edges_of_node(self):
        allOut = self.graph.all_out_edges_of_node(0)
        outNodes = {4: [4, 7.4]}
        self.assertDictEqual(allOut, outNodes)

    def test_add_node(self):
        self.graph.add_node(1)
        self.graph.add_node(3)
        self.graph.add_node(5)
        self.assertEqual(7, len(self.graph.nodes))

    def test_remove_node(self):
        self.graph.remove_node(0)
        self.assertEqual(3, len(self.graph.nodes))

    def test_add_edge(self):
        self.graph.add_edge(0, 1, 0)
        self.assertEqual(4, len(self.graph.edges))
        self.graph.add_edge(6, 0, 0) # need to remain 4, edge exist!
        self.assertEqual(4, len(self.graph.edges))
        self.graph.add_edge(52, 1, 0) # need to remain 4, node do not exist!
        self.assertEqual(4, len(self.graph.edges))

    def test_remove_edge(self):
        self.graph.remove_edge(6, 0)
        self.assertEqual(3, len(self.graph.edges))
        self.graph.remove_edge(6, 0)
        self.assertEqual(3, len(self.graph.edges))

if __name__ == '__main__':
    unittest.main()