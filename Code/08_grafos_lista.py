from queue import Queue

# Grafo como Lista de Adjacências

# Lista ligada de arestas / adjacências de um vértice dirigido ou não
class Adjacencia:
    def __init__(self, vertice, peso, prox):
        self.vertice = vertice
        self.peso = peso
        self.prox = prox

class Vertice:
    def __init__(self, info, cabeca):
        self.info = info
        self.cabeca = cabeca  # primeira aresta

class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices  # Número delimitado de vértices
        self.arestas = 0
        self.arr_vertices = [Vertice(None, None) for _ in range(vertices)]

    def criar_aresta(self, vertice_ini, vertice_fim, peso):
        nova_adj = Adjacencia(
            vertice_fim, peso, self.arr_vertices[vertice_ini].cabeca)
        self.arr_vertices[vertice_ini].cabeca = nova_adj
        self.arestas = self.arestas + 1
        return True

    def set_info_vertice(self, v, info):
        self.arr_vertices[v].info = info

    def imprimir(self):
        for i in self.arr_vertices:
            adj = i.cabeca
            while adj != None:
                print("Nó", i.info, "vai para nó", 
                self.arr_vertices[adj.vertice].info, "com peso", 
                adj.peso)
                adj = adj.prox
        print()

    def visita_profundidade(self, ini, cor, info):
        if ini == None: return False
        print("Visita nó", self.arr_vertices[ini].info)

        if self.arr_vertices[ini].info == info:
            print("Achou nó", info)
            return True
        
        cor[ini] = 1
        v = self.arr_vertices[ini].cabeca
        
        while v != None:
            if cor[v.vertice] == 0:
                achou = g.visita_profundidade(v.vertice, cor, info)
                if not(achou is False): return achou
            v = v.prox
        
        cor[ini] = 2
        return False

    def busca_profundidade(self, info):
        cor = [0 for _ in range(self.vertices)]
        for u in range(self.vertices):
            if cor[u] == 0:
                achou = g.visita_profundidade(u, cor, info)
                if not(achou is False): return achou
                print("----")
        return False


    def visita_largura(self, explorados, u, info):            
        f = Queue(self.vertices)
        f.put(u)

        while not(f.empty()):
            u = f.get()
            v = g.arr_vertices[u].cabeca
            print('Visita nó', g.arr_vertices[u].info)
            
            if self.arr_vertices[u].info == info:
                print('Achou nó', info)
                return True
            
            explorados[u] = True
            while v:
                if explorados[v.vertice] is False:
                    explorados[v.vertice] = True
                    f.put(v.vertice)
                v = v.prox

        return False

    def busca_largura(self, info):
        explorados = [False for _ in range(self.vertices)]

        for u in range(self.vertices):
            if explorados[u] == False:
                achou = g.visita_largura(explorados, u, info)
                if achou is True: return achou
            print("----")
        
        return False

if __name__ == "__main__":
    g = Grafo(10)
    
    for i in range(10):
        g.set_info_vertice(i, chr(65+i)) #chr(65) == A
    
    g.criar_aresta(2, 4, 20)
    g.criar_aresta(2, 5, 2)
    g.criar_aresta(2, 1, 30)
    g.criar_aresta(7, 0, 5)
    g.criar_aresta(7, 7, 0)
    g.imprimir()
    print(g.busca_profundidade('J'))
    print()
    print(g.busca_profundidade('E'))
    print()
    print(g.busca_profundidade('L'))
    print()

    print(g.busca_largura('J'))
    print()
    print(g.busca_largura('E'))
    print()
    print(g.busca_largura('L'))
    print()