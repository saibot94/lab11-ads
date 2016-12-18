import unittest
from lists.lista_simpla import ListaSimpluInlantuita


class TestListaSimpla(unittest.TestCase):
    def setUp(self):
        self.lista = ListaSimpluInlantuita()

    def tearDown(self):
        del self.lista
