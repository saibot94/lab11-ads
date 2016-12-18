import unittest
from lists.lista_simpla import ListaSimpluInlantuita


class TestListaSimpla(unittest.TestCase):
    def setUp(self):
        self.lista = ListaSimpluInlantuita()

    def tearDown(self):
        del self.lista

    def test_adaugare_fata(self):
        self.lista.adaugareFata('a')
        self.lista.adaugareFata('b')
        self.assertEqual('b', self.lista.inceput.info)
        self.assertEqual('a', self.lista.inceput.urm.info)

    def test_adaugare_spate(self):
        self.lista.adaugareSpate('a')
        self.lista.adaugareSpate('b')
        self.assertEqual('b', self.lista.inceput.urm.info)
        self.assertEqual('a', self.lista.inceput.info)

    def test_adaugare_dupa_elem_ok(self):
        self.lista.adaugareSpate('a')
        self.lista.adaugareDupaElement('a', 'b')
        self.assertEqual('b', self.lista.inceput.urm.info)

    def test_adaugare_dupa_elem_not_ok(self):
        self.lista.adaugareSpate('a')
        self.lista.adaugareDupaElement('c', 'b')
        self.assertEqual(None, self.lista.inceput.urm)

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

    def test_sterge_dupa_element(self):
        self.lista.adaugareFata('a')
        self.lista.adaugareFata('b')
        self.lista.adaugareFata('c')
        self.lista.stergereDupaElement('c')

        self.assertEquals('a', self.lista.inceput.urm.info)

    def test_cautare_element(self):
        self.lista.adaugareFata('a')
        self.lista.adaugareFata('b')
        self.lista.adaugareFata('c')

        self.assertTrue(self.lista.cautareElement('c'))
        self.assertFalse(self.lista.cautareElement('d'))

    def test_cautare_index(self):
        self.lista.adaugareFata('a')
        self.lista.adaugareFata('b')
        self.lista.adaugareFata('c')

        self.assertTrue(self.lista.cautareDupaIndex(3).info == 'a')
        self.assertTrue(self.lista.cautareDupaIndex(2).info == 'b')
        self.assertTrue(self.lista.cautareDupaIndex(6) is None)
