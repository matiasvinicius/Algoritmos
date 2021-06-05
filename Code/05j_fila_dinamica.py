class Registro:
    def __init__(self, id, chave):
        self.id = id,
        self.chave = chave

class Elemento:
    def __init__(self, reg, prox):
        self.reg = reg
        self.prox = prox

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def tamanho(self):
        i = self.inicio
        tam = 0
        while i != None:
            tam += 1
            i = i.prox
        return tam

    def imprimir(self):
        i = self.inicio
        print("Fila:")
        while i != None:
            print("ID:", i.reg.id, 
            "Chave:", i.reg.chave)
            i = i.prox
        print("Fim da Fila")
    
    def inserir(self, reg):
        novo = Elemento(reg, None)
        if self.fim == None: 
            self.inicio = novo
        else:
            self.fim.prox = novo
        self.fim = novo
        return True

    def excluir(self):
        if self.inicio == None:
            return False
        removed = self.inicio
        self.inicio = self.inicio.prox
        del removed
        if self.inicio == None:
            self.fim = None
        return True
    
    def reinicializar(self):
        self.inicio = None
        self.fim = None

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
