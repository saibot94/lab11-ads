import unittest
from lists.lista_dubla import ListaDubluInlantuita


class TestListaDubla(unittest.TestCase):
    def setUp(self):
        self.lista = ListaDubluInlantuita()

    def tearDown(self):
        del self.lista

    def test_adaugare_fata(self):
        self.lista.adaugareFata('a')
        self.lista.adaugareFata('b')
        self.assertEqual('b', self.lista.inceput.info)
        self.assertEqual('a', self.lista.sfarsit.info)

    def test_adaugare_spate(self):
        self.lista.adaugareSpate('a')
        self.lista.adaugareSpate('b')
        self.assertEqual('a', self.lista.inceput.info)
        self.assertEqual('b', self.lista.sfarsit.info)

    def test_sterge_fata(self):
        self.lista.adaugareFata('a')
        self.lista.adaugareFata('b')
        self.lista.stergeFata()

        self.assertEquals('a', self.lista.inceput.info)

    def test_sterge_spate(self):
        self.lista.adaugareFata('a')
        self.lista.adaugareFata('b')
        self.lista.stergeSpate()

        self.assertEquals('b', self.lista.inceput.info)
        self.assertEquals(None, self.lista.inceput.urm)
