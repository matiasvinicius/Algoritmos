MAX = 50

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
        self.elemento = [Elemento] * MAX
        self.inicio = None
        self.dispo = None

    def inicializar_lista(self):
        for i in range(MAX-1):
            self.elemento[i] = Elemento(Registro, i+1)
        self.elemento[MAX-1].prox = None
        self.inicio = None
        self.dispo = 0

    def tamanho(self):
        i = self.inicio
        tamanho = 0
        while i != None:
            tamanho +=1
            i = self.elemento[i].prox
        return tamanho

    def imprimir_lista(self):
        i = self.inicio
        print("Lista de Registros")
        while i != None:
            print("ID:", self.elemento[i].reg.id,
            "Chave:", self.elemento[i].reg.chave)
            i = self.elemento[i].prox

    def busca(self, id):
        i = self.inicio
        while (i != None and self.elemento[i].reg.id < id):
            i = self.elemento[i].prox
        if (i != None and self.elemento[i].reg.id == id):
            return i

    def obter_no(self):
        resultado = self.dispo
        if self.dispo != None:
            self.dispo = self.elemento[self.dispo].prox
        return resultado

    def inserir(self, reg):
        if (self.dispo == None): return False
        ant = None
        i = self.inicio
        id = reg.id
        while (i != None and self.elemento[i].reg.id < id):
            ant = i
            i = self.elemento[i].prox
        if (i != None and self.elemento[i].reg.id == id): return False
        i = self.obter_no()
        self.elemento[i].reg = reg
        if ant == None:
            self.elemento[i].prox = self.inicio
            self.inicio = i
        else:
            self.elemento[i].prox = self.elemento[ant].prox
            self.elemento[ant].prox = i
        return True   

    def devolver_no(self, posicao):
        self.elemento[posicao].prox = self.dispo
        self.dispo = posicao

    def excluir(self, id):
        ant = None
        i = self.inicio
        while (i != None) and (self.elemento[i].reg.id < id):
            ant = i
            i = self.elemento[i].prox
        if (i == None or self.elemento[i].reg.id != id): return False
        if ant == None:
            self.inicio = self.elemento[i].prox
        else: self.elemento[ant].prox = self.elemento[i].prox        
        self.devolver_no(i)
        return True
    
    def reinicializar_lista(self):
        self.inicializar_lista()

if __name__ == "__main__":
    #Exemplo de uso
    reg1 = Registro(1, 'b8')
    reg2 = Registro(2, 'a3')
    reg3 = Registro(3, 'a5')
    reg4 = Registro(4, 'b1')

    l = Lista()
    l.inicializar_lista()
    l.inserir(reg2)
    l.inserir(reg4)
    l.inserir(reg3)
    l.inserir(reg1)
    l.imprimir_lista()
    print(l.excluir(2))
    print(l.excluir(20))
    l.imprimir_lista()
    l.reinicializar_lista()
    l.imprimir_lista()

        

    
    