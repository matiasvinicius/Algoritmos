MAX = 50

class Registro:
    def __init__(self, id, chave):
        self.id = id
        self.chave = chave

class Pilha:
    def __init__(self):
        self.reg = [Registro] * MAX
        self.topo = -1

    def tamanho(self):
        return self.topo + 1

    def imprimir(self):
        print("PILHA:")
        i = self.topo
        while i >= 0:
            print("ID", self.reg[i].id,
            "Chave:", self.reg[i].chave)
            i -= 1

    def push(self, reg):
        if self.topo >= MAX-1: return False
        self.topo = self.topo + 1
        self.reg[self.topo] = reg
        return True

    def pop (self):
        if self.topo == -1: return False
        removed = self.reg[self.topo]
        self.topo = self.topo - 1
        return removed
    
    def reinicializar(self):
        self.topo = -1

if __name__ == "__main__":
    reg1 = Registro(1, 'b8')
    reg2 = Registro(2, 'a3')
    reg3 = Registro(3, 'a5')
    reg4 = Registro(4, 'b1')
    
    p = Pilha()
    p.push(reg1)
    p.push(reg2)
    p.push(reg3)
    p.push(reg4)
    p.pop()
    p.imprimir()
    p.reinicializar()
    p.imprimir()