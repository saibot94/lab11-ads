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
        if self.inceput.urm is None:
            self.inceput = None
        else:
            aux = self.inceput
            while aux.urm.urm is not None:
                aux = aux.urm
            aux.urm = None

    def stergereDupaElement(self, x):
        aux = self.inceput
        while aux is not None and aux.info != x:
            aux = aux.urm
        if aux is not None and aux.urm is not None:
            aux.urm = aux.urm.urm
        else:
            print 'Nu exista un not cu informatia ', x

    def cautareElement(self, x):
        aux = self.inceput
        while aux is not None and aux.info != x:
            aux = aux.urm
        return aux is not None

    def cautareDupaIndex(self,k):
        aux = self.inceput
        i = 1
        while aux is not None and i < k:
            aux = aux.urm
            i += 1
        return aux


