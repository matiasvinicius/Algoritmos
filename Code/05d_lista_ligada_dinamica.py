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
    
    def tamanho(self):
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

    def inserir(self, chave):
        anterior, atual = self.busca_dupla(chave)
        if atual == 


if __name__ == "__main__":
    l = Lista()