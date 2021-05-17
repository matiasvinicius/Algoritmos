class Registro:
    def __init__(self, id, chave):
        self.id = id
        self.chave = chave

class Lista_Linear_Sequencial:
    def __init__(self, max):
        self.registro = [Registro] * (max+1)
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

    def busca_sentinela(self, id):
        i = 0
        self.registro[self.n_elementos].id = id
        while self.registro[i].id != id: i += 1
        if i == self.n_elementos: return -1        
        return i

    def inserir_registro_ord(self, registro):
        if self.n_elementos >= self.max:
            return False

        pos = self.n_elementos
        while (pos > 0 and 
        self.registro[pos-1].id > registro.id):
            self.registro[pos] = self.registro[pos-1]
            pos -= 1
        self.registro[pos] = registro
        self.n_elementos += 1
        return True

    def busca_binaria(self, id):
        esq = 0
        dir = self.n_elementos-1
        
        while esq <= dir:
            meio = int((esq+dir)/2)
            if self.registro[meio].id == id: return meio 
            elif self.registro[meio].id < id: 
                esq = meio + 1
            else:
                dir = meio -1
        
        return -1 


    def excluir_elemento(self, chave):
        posicao = self.busca_binaria(chave)
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

    l.inserir_registro_ord(reg1)
    l.inserir_registro_ord(reg2)
    l.inserir_registro_ord(reg3)
    l.inserir_registro_ord(reg4)
    l.imprimir_lista()
    
    print(l.busca_binaria(4))

    print(l.busca_sentinela(4))

    l.excluir_elemento(4)
    l.imprimir_lista()
