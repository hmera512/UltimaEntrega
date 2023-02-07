import hashlib
import random

class Usuario:
    seudoNombre = int
    def __init__(self) :
        self.seudoNombre = random.randrange(10000,20000)
        pass
    def getSeudo(self):
        return self.seudoNombre
        pass
    pass