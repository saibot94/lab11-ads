from nod import Nod


class ListaSimpluInlantuita:
    def __init__(self):
        self.inceput = None

    def adaugareFata(self, x):
        if self.inceput is None:
            self.inceput = Nod(x, None)
        else:
            newNode = Nod(x, self.inceput)
            self.inceput = newNode

    def adaugareSpate(self, x):
        if self.inceput is None:
            self.inceput = Nod(x, None)
        else:
            aux = self.inceput
            while aux.urm is not None:
                aux = aux.urm
            newNode = Nod(x, None)
            aux.urm = newNode

    def adaugareDupaElement(self, x, y):
        aux = self.inceput
        while aux is not None and aux.info != x:
            aux = aux.urm
        if aux is not None:
            nodNou = Nod(y, aux.urm)
            aux.urm = nodNou
        else:
            print 'Nu exista nodul'

    def stergeFata(self):
        if self.inceput is not None:
            self.inceput = self.inceput.urm
        else:
            print 'lista este goala'

    def stergeSpate(self):
        pass
