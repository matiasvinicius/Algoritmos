import gc

class Registro:
    def __init__(self, id, chave):
        self.id = id
        self.chave = chave

class Elemento:
    def __init__(self, reg, ant, prox):
        self.reg = reg
        self.ant = ant
        self.prox = prox

class Deque:
    def __init__(self):
        self.cabeca = Elemento(Registro, 
        Elemento, Elemento)
        self.cabeca.ant = self.cabeca
        self.cabeca.prox = self.cabeca
    
    def tamanho(self):
        i = self.cabeca.prox
        tam = 0
        while i != self.cabeca:
            tam += 1
            i = i.prox
        return tam

    def imprimir(self):
        i = self.cabeca.ant
        print("Deque (fim -> início):")
        while i != self.cabeca:
            print("ID:", i.reg.id, 
            "Chave", i.reg.chave)
            i = i.ant
        print("Fim do Deque")

    def inserir_fim(self, reg):
        novo = Elemento(reg, 
        self.cabeca.ant, self.cabeca)
        self.cabeca.ant = novo
        novo.ant.prox = novo
        return True
    
    def excluir_inicio(self):
        if self.cabeca.prox == self.cabeca:
            return False
        removed = self.cabeca.prox
        self.cabeca.prox = removed.prox
        removed.prox.ant = self.cabeca
        del removed
        return True

    def reinicializar(self):
        self.cabeca.prox = self.cabeca
        self.cabeca.ant = self.cabeca
        gc.collect()
        return True

if __name__ == "__main__":  
    reg1 = Registro(1, 'b8')
    reg2 = Registro(2, 'a3')
    reg3 = Registro(3, 'a5')
    reg4 = Registro(4, 'b1')
    d = Deque()
    print("Cabeça: ", d.cabeca)
    print("Cabeça -> ant: ", d.cabeca.ant)
    print("Cabeça -> prox: ", d.cabeca.prox)
    print("Tamanho:", d.tamanho())
    d.imprimir()
    print("Inserção no fim: ", d.inserir_fim(reg1))
    print("Tamanho:", d.tamanho())
    print("Inserção no fim: ", d.inserir_fim(reg2))
    print("Inserção no fim: ", d.inserir_fim(reg3))
    print("Inserção no fim: ", d.inserir_fim(reg4))
    d.imprimir()
    print("Remoção no início: ", d.excluir_inicio())
    d.imprimir()
    print("Reinicialização: ", d.reinicializar())
    d.imprimir()
