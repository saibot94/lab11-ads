from nod import NodDublu as Nod


class ListaDubluInlantuita:
    def __init__(self):
        self.inceput = None
        self.sfarsit = None

    def adaugareFata(self, x):
        if self.inceput is None:
            ref = Nod(x, None, None)
            self.inceput = ref
            self.sfarsit = ref
        else:
            ref = Nod(x, None, None)
            ref.urm = self.inceput
            self.inceput.prec = ref
            self.inceput = ref

    def adaugareSpate(self, x):
        if self.inceput is None:
            ref = Nod(x, None, None)
            self.inceput = ref
            self.sfarsit = ref
        else:
            ref = Nod(x, None, None)
            ref.prec = self.sfarsit
            self.sfarsit.urm = ref
            self.sfarsit = ref

    def inserareDupa(self, adr, x):
        ref = Nod(x, None, None)
        ref.urm = adr.urm
        ref.prec = adr
        adr.urm = ref
        ref.urm.prec = ref

    def inserareInainte(self, adr, x):
        ref = Nod(x, None, None)
        ref.urm = adr
        ref.prec = adr.prec
        adr.prec = ref
        ref.prec.urm = ref

    def stergeSpate(self):
        if self.inceput is not None:
            if self.inceput == self.sfarsit:
                self.inceput = None
                self.sfarsit = None
            else:
                self.sfarsit = self.sfarsit.prec
                self.sfarsit.urm = None
        else:
            print 'Lista este goala'

    def stergeFata(self):
        if self.inceput is not None:
            if self.inceput == self.sfarsit:
                self.inceput = None
                self.sfarsit = None
            else:
                self.inceput = self.inceput.urm
                self.inceput.prec = None
        else:
            print 'Lista este goala'

    def stergereElement(self, adr):
        if adr.urm is not None:
            adr.urm.prec = adr.prec
        else:
            self.sfarsit = adr.prec
        if adr.prec is not None:
            adr.prec.urm = adr.urm
        else:
            self.inceput = adr.urm


