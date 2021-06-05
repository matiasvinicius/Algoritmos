MAX = 50

class Registro:
    def __init__(self, id, chave):
        self.id = id,
        self.chave = chave

class Fila:
    def __init__(self):
        self.reg = [Registro] * MAX
        self.inicio = 0
        self.n_elementos = 0
    
    def tamanho(self):
        return self.n_elementos
    
    def imprimir(self):
        i = self.inicio
        print("Fila")
        for _ in range(self.tamanho()):
            print("ID:", self.reg[i].id,
            "Chave:", self.reg[i].chave)
            i = (i + 1) % MAX
        
    def inserir(self, reg):
        if self.n_elementos == MAX:
            return False
        i = (self.inicio + self.n_elementos) % MAX
        self.reg[i] = reg
        self.n_elementos = self.n_elementos + 1
        return True

    def excluir(self):
        if self.n_elementos == 0: 
            return False
        self.inicio = (self.inicio + 1) % MAX
        self.n_elementos = self.n_elementos - 1
        return True
    
    def reinicializar(self):
        self.inicio = 0
        self.n_elementos = 0


if __name__ == "__main__":
    reg1 = Registro(1, 'b8')
    reg2 = Registro(2, 'a3')
    reg3 = Registro(3, 'a5')
    reg4 = Registro(4, 'b1')
    f = Fila()
    print("Tamanho:", f.tamanho())    
    print("Inserção:", f.inserir(reg1))
    print("Inserção:", f.inserir(reg2))
    print("Inserção:", f.inserir(reg3))
    print("Inserção:", f.inserir(reg4))
    f.imprimir()
    print("Remoção:", f.excluir())
    f.imprimir()
    print("Remoção:", f.excluir())
    print("Inserção:", f.inserir(reg1))
    f.imprimir()
    print("Remoção:", f.excluir())
    print("Remoção:", f.excluir())
    print("Remoção:", f.excluir())
    print("Remoção:", f.excluir())
    print("Tamanho:", f.tamanho())
