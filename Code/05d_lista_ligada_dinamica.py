class Registro:
    def __init__(self, id, chave):
        self.id = id
        self.chave = chave

class Elemento:
    def __init__(self, registro, prox):
        self.reg = registro
        self.prox = prox

class Lista:
    def __init__(self):
        self.inicio = None        
    
    def inicializar_lista(self):
        self.inicio = None

    def tamanho(self):
        endereco = self.inicio
        tamanho = 0
        while endereco != None:
            tamanho += 1
            endereco = endereco.prox
        return tamanho
    
    def imprimir_lista(self):
        endereco = self.inicio
        print("Lista de Registros")
        while endereco != None:
            print("ID:", endereco.reg.id, "Chave:", endereco.reg.chave)
            endereco = endereco.prox

    def busca(self, chave):
        posicao = self.inicio
        while posicao != None:
            if posicao.reg.chave == chave:
                return posicao
            posicao = posicao.prox
        return None

    def busca_dupla(self, chave):
        atual = self.inicio
        anterior = None
        while atual != None:
            if atual.reg.chave == chave:
                return anterior, atual
            anterior = atual
            atual = atual.prox
        return None, None

    def inserir(self, reg):
        chave = reg.chave
        anterior, atual = self.busca_dupla(chave)
        if atual != None: return False
        if anterior == None:
            novo = Elemento(reg, l.inicio)
            self.inicio = novo
        else:
            novo = Elemento(reg, anterior.prox)
            anterior.prox = novo        
        return True

    def excluir(self, chave):
        anterior, atual = self.busca_dupla(chave)
        if atual == None: return False
        if anterior == None: 
            self.inicio = atual.prox
        else: 
            anterior.prox = atual.prox
        return True

    #Não é possível limpar explicitamente a memória 
    #de objetos em Python, então devemos apenas
    #perder a referência à eles e o garbage collector
    #irá removê-los em algum momento
    def reinicializar_lista(self):
        self.inicio = None
        return 0

if __name__ == "__main__":
    l = Lista()
    reg1 = Registro(1, 'b8')
    reg2 = Registro(2, 'a3')
    reg3 = Registro(3, 'a5')
    reg4 = Registro(4, 'b1')

    l = Lista()
    l.inicializar_lista()
    l.inserir(reg2)
    l.inserir(reg1)
    l.inserir(reg3)
    l.inserir(reg4)
    l.inserir(reg4)
    l.imprimir_lista()
    l.excluir('b7')
    l.excluir('b8')
    l.imprimir_lista()
    l.reinicializar_lista()
    l.imprimir_lista()
    l.inserir(reg2)
    l.imprimir_lista()

