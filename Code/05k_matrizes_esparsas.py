class Registro:
    def __init__(self, id, chave):
        self.id = id
        self.chave = chave

class No:
    def __init__(self, reg, coluna, prox):
        self.registro = reg
        self.coluna = coluna
        self.prox = prox 

class Matriz:
    def __init__(self, linhas, colunas):
        self.A = [No] * linhas
        for i in range(linhas): self.A[i] = None
        self.linhas = linhas
        self.colunas = colunas

    def atribuir(self, linha, coluna, reg):
        if (linha < 0 or
        linha >= self.linhas or
        coluna < 0 or
        coluna >= self.colunas):
            return False
        anterior = None
        atual = self.A[linha]
        
        while (atual != None and
        atual.coluna < coluna):
            anterior = atual
            autal = atual.prox

        if (atual != None 
        and atual.coluna == coluna):
            if reg.id == 0:
                if anterior == None:
                    self.A[linha] = atual.prox
                else:
                    anterior.prox = atual.prox
                del atual
            else:
                atual.reg = reg
        
        else:
            novo = No(reg, coluna, atual)
            if anterior == None:
                self.A[linha] = novo
            else:
                anterior.prox = novo

        return True

    def acessar(self, linha, coluna):
        if (linha < 0 or 
        linha >= self.linhas or
        coluna < 0 or
        coluna >= self.colunas):
            return -1

        atual = self.A[linha]
        while (atual != None and
        atual.coluna < coluna):
            atual = atual.prox
        if (atual != None and
        atual.coluna == coluna):
            return atual.registro
        else: return -1

if __name__ == "__main__":
    reg1 = Registro(1, 'b8')
    reg2 = Registro(2, 'a3')
    reg3 = Registro(3, 'a5')
    reg4 = Registro(4, 'b1')
    reg0 = Registro(0, None)
    
    m = Matriz(10, 20)
    print("Acesso", m.acessar(1,2))
    print("Atribuição[1,2]", m.atribuir(1,2, reg1))
    print("Chave [1,2]", m.acessar(1,2).chave)
    print("Registro [0,2]", m.acessar(0,2))
    print("Remoção [1,2]", m.atribuir(1,2, reg0))
    print("Registro [1,2]", m.acessar(1,2))
