import unittest
from lists.nod import Nod


class TestNodes(unittest.TestCase):
    def test_nodes_equal(self):
        n1 = Nod(3, None)
        n2 = Nod(3, None)
        self.assertEqual(n1.info, n2.info)

    def test_next_node(self):
        n1 = Nod(3, None)
        n2 = Nod(3, n1)
        self.assertEqual(n1.info, n2.urm.info)
