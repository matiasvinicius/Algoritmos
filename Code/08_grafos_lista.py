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
                print("Nó", i.info, "vai para nó", self.arr_vertices[adj.vertice].info, "com peso", adj.peso)
                adj = adj.prox
        print()



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