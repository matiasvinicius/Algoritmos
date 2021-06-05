class Registro:
    def __init__(self, id, chave):
        self.id = id
        self.chave = chave

class Elemento:
    def __init__(self, reg, prox):
        self.reg = reg
        self.prox = prox

class Lista:
    def __init__(self):
        self.cabeca = None

    def inicializar_lista(self):
        self.cabeca = Elemento(Registro, Elemento)
        self.cabeca.prox = self.cabeca

    def tamanho(self):
        i = self.cabeca.prox
        tam = 0
        while i != self.cabeca:
            tam += 1
            i = i.prox
        return tam

    def imprimir_lista(self):
        i = self.cabeca.prox
        print("Lista de Registros")
        while i != self.cabeca:
            print("ID: ", i.reg.id, "Chave: ", i.reg.chave)
            i = i.prox

    def busca_sentinela(self, id):
        i = self.cabeca.prox
        self.cabeca.reg.id = id
        while i.reg.id < id:
            i = i.prox
        if i != self.cabeca and i.reg.id == id: return i
        return None

    def busca_dupla(self, id):
        anterior = self.cabeca
        i = self.cabeca.prox
        self.cabeca.reg.id = id
        while i.reg.id < id:
            anterior = i
            i = i.prox
        if i != self.cabeca and i.reg.id == id: 
            return anterior, i
        return anterior, None

    def inserir(self, reg):
        anterior, i = self.busca_dupla(reg.id)
        if i != None: return False
        novo = Elemento(reg, anterior.prox)
        anterior.prox = novo

    def excluir(self, id):
        anterior, i = self.busca_dupla(id)
        if i == None: return False
        anterior.prox = i.prox
        del i
        return True
    
    def reinicializar_lista(self):
        self.cabeca.prox = self.cabeca

if __name__ == "__main__":
    reg1 = Registro(1, 'b8')
    reg2 = Registro(2, 'a3')
    reg3 = Registro(3, 'a5')
    reg4 = Registro(4, 'b1')
    
    l = Lista()
    l.inicializar_lista()
    print(l.cabeca.prox)
    l.imprimir_lista()
    l.inserir(reg2)
    l.inserir(reg1)
    l.inserir(reg3)
    l.inserir(reg4)
    l.inserir(reg4)
    l.imprimir_lista()
    l.excluir(1)
    l.excluir(4)
    l.imprimir_lista()
    l.reinicializar_lista()
    l.imprimir_lista()