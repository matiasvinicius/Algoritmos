class Registro:
    def __init__(self, id, chave):
        self.id = id
        self.chave = chave

class Elemento:
    def __init__(self, reg, prox):
        self.reg = reg
        self.prox = prox

class Pilha:
    def __init__(self):
        self.topo = None

    def tamanho(self):
        i = self.topo
        tam = 0
        while i != None:
            tam += 1
            i = i.prox
        return tam

    def esta_vazia(self):
        if self.topo == None: return True
        return False

    def imprimir(self):
        i = self.topo
        print("PILHA")
        while i != None:
            print("ID", i.reg.id, "Chave", i.reg.chave)
            i = i.prox

    def push(self, reg):
        novo = Elemento(reg, self.topo)
        self.topo = novo
        return True

    def pop(self):
        removed = self.topo.reg
        self.topo = self.topo.prox
        del removed
        return True

    def reinicializar(self):
        self.topo = None

if __name__ == "__main__":
    reg1 = Registro(1, 'b8')
    reg2 = Registro(2, 'a3')
    reg3 = Registro(3, 'a5')
    reg4 = Registro(4, 'b1')

    p = Pilha()
    print(p.esta_vazia())
    p.push(reg1)
    print(p.esta_vazia())
    p.push(reg2)
    p.push(reg3)
    p.push(reg4)
    print(p.tamanho())
    p.pop()
    p.imprimir()
    p.reinicializar()
    p.imprimir()