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
        self.assertEquals(self.lista.sfarsit.info, self.lista.inceput.info)

    def test_stergere_ref_mijloc(self):
        self.lista.adaugareSpate('a')
        self.lista.adaugareSpate('b')
        self.lista.adaugareSpate('c')

        elem = self.lista.inceput.urm
        self.lista.stergereElement(elem)
        self.assertEqual(self.lista.inceput.info, 'a')
        self.assertEqual(self.lista.sfarsit.info, 'c')

    def test_stergere_ref_fata(self):
        self.lista.adaugareSpate('a')
        self.lista.adaugareSpate('b')
        self.lista.adaugareSpate('c')

        elem = self.lista.inceput
        self.lista.stergereElement(elem)
        self.assertEqual(self.lista.inceput.info, 'b')
        self.assertEqual(self.lista.sfarsit.info, 'c')

    def test_stergere_ref_spate(self):
        self.lista.adaugareSpate('a')
        self.lista.adaugareSpate('b')
        self.lista.adaugareSpate('c')

        elem = self.lista.sfarsit
        self.lista.stergereElement(elem)
        self.assertEqual(self.lista.inceput.info, 'a')
        self.assertEqual(self.lista.sfarsit.info, 'b')

    def test_inserare_inainte(self):
        self.lista.adaugareSpate('a')
        self.lista.adaugareSpate('b')
        self.lista.adaugareSpate('c')

        elem = self.lista.sfarsit.prec
        self.lista.inserareInainte(elem, 'd')
        self.assertEqual(self.lista.inceput.urm.info, 'd')

    def test_inserare_dupa(self):
        self.lista.adaugareSpate('a')
        self.lista.adaugareSpate('b')
        self.lista.adaugareSpate('c')

        elem = self.lista.sfarsit.prec
        self.lista.inserareDupa(elem, 'd')
        self.assertEqual(self.lista.inceput.urm.urm.info, 'd')
