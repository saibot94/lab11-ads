class Nod:
    def __init__(self, info, urm):
        self.info = info
        self.urm = urm

    def __repr__(self):
        return str(self.info)


if __name__ == '__main__':
    print Nod(30)
