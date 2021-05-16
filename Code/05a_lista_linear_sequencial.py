class Registro:
    def __init__(self, id, chave):
        self.id = id
        self.chave = chave

class Lista_Linear_Sequencial:
    def __init__(self, max):
        self.registro = [Registro] * max
        self.n_elementos = -1
        self.max = max

    def inicializar_lista(self):
        self.n_elementos = 0

    def tamanho(self):
         return self.n_elementos

    def imprimir_lista(self):
        print("LISTA de", self.n_elementos, "registros")
        
        for i in range(self.n_elementos):
            print("Elemento:", i, 
            "| ID:", self.registro[i].id, 
            "| Chave:", self.registro[i].chave)

    def busca_sequencial(self, chave):
        for i in range(self.n_elementos):
            if self.registro[i].chave == chave:
                return i
        return -1

    def inserir_registro(self, registro, posicao):
        if self.n_elementos == max or posicao < 0 or posicao > self.n_elementos:
            return False

        j = self.n_elementos
        while j > posicao:
            self.registro[j] = self.registro[j-1]
            j -= 1
        self.registro[posicao] = registro
        self.n_elementos += 1
        return True

    def excluir_elemento(self, chave):
        posicao = self.busca_sequencial(chave)
        if posicao == -1: return False

        j = posicao
        while j < self.n_elementos-1:
            self.registro[j] = self.registro[j+1]
            j += 1
        self.n_elementos -= 1
        return True

    def reinicializar_lista(self):
        self.n_elementos = 0

if __name__ == "__main__":
    #Exemplo de uso
    
    reg1 = Registro(1, 'b8')
    reg2 = Registro(2, 'a3')
    reg3 = Registro(3, 'a5')
    reg4 = Registro(4, 'b1')

    l = Lista_Linear_Sequencial(50)
    
    l.inicializar_lista()
    l.imprimir_lista()

    l.inserir_registro(reg1, 0)
    l.inserir_registro(reg2, 1)
    l.inserir_registro(reg3, 1)
    l.inserir_registro(reg4, 1)
    l.imprimir_lista()
    
    print(l.excluir_elemento('b8'))
    l.imprimir_lista()

    l.reinicializar_lista()
    l.imprimir_lista()
