from queue import Queue

class No:
    def __init__(self, ch):
        self.chave = ch
        self.esq = None
        self.dir = None

def adicionar(raiz, no):
    if raiz == None: 
        print("Troca ", raiz, "por", no.chave)
        return no
    if no.chave < raiz.chave:
        print("Nó", no.chave, "< raíz", raiz.chave)
        raiz.esq = adicionar(raiz.esq, no)
    else:
        print("Nó", no.chave, "> raíz", raiz.chave)
        raiz.dir = adicionar(raiz.dir, no)
    return raiz

def busca(raiz, chave):
    if raiz == None:
        return None
    if raiz.chave == chave:
        return raiz
    if raiz.chave > chave:
        return busca(raiz.esq, chave)
    return busca(raiz.dir, chave)

def n_nos(raiz):
    if not(raiz): return 0
    return n_nos(raiz.esq) + 1 + n_nos(raiz.dir)

def busca_no_e_pai(raiz, ch):
    filho = raiz
    pai = None
    while filho != None:
        if filho.chave == ch:
            return pai, filho
        pai = filho
        if ch < filho.chave:
            filho = filho.esq
        else: 
            filho = filho.dir    
    return None, None 

#NÃO CONFIÁVEL - ver remover() em 07_avl.py
def remove_no(raiz, ch):
    pai, no = busca_no_e_pai(raiz, ch)
    if no == None: 
        return raiz
    if no.esq != None:
        q = no.dir
    elif no.dir != None:
        q = no.esq
    else:
        p = no
        q = no.esq
        while q.dir != None:
            p = q
            q = q.dir
        if p != no:
            p.dir = q.esq
            q.esq = no.esq
        q.dir = no.dir
        if pai != None:
            return q
        if ch < pai.chave: pai.esq = q
        else: pai.dir = q
    return raiz

def pre_ordem(raiz):
    if raiz == None: return
    print(raiz.chave)
    pre_ordem(raiz.esq)
    pre_ordem(raiz.dir)

def em_odem(raiz):
    if raiz == None: return
    em_odem(raiz.esq)
    print(raiz.chave)
    em_odem(raiz.dir)

def pos_ordem(raiz):
    if raiz == None: return
    pos_ordem(raiz.esq)
    pos_ordem(raiz.dir)
    print(raiz.chave)

def pre_ordem_iter(raiz):
    if raiz == None: return
    pilha = []
    pilha.append(raiz)
    while len(pilha) > 0:
        atual = pilha[-1]
        pilha.pop()
        print(atual.chave)
        if atual.dir != None:
            pilha.append(atual.dir)
        if atual.esq != None:
            pilha.append(atual.esq)

def em_nivel(raiz):
    if raiz == None: return
    q = Queue()
    q.put(raiz)
    while not(q.empty()):
        atual = q.get()
        print(atual.chave)
        if atual.esq: q.put(atual.esq)
        if atual.dir: q.put(atual.dir)

def imprimir(raiz):
    if raiz != None:
        print(raiz.chave, '(', end='')
        imprimir(raiz.esq), 
        imprimir(raiz.dir), 
        print(')', end='')

def inserir_no(raiz, ch):
    if raiz == None:
        return No(ch)
    if raiz.chave >= ch: 
        raiz.esq = inserir_no(raiz.esq, ch)
    else:
        raiz.dir = inserir_no(raiz.dir, ch)
    return raiz

#NÃO CONFIÁVEL - ver remover() em 07_avl.py
def excluir_no(raiz, chave):
    atual = raiz
    if atual == None: return False
    
    if atual.chave == chave:
        if atual.esq or atual.dir:
            if atual.esq: return atual.esq
            return atual.dir
        
        substituto, pai_substituto = maior_esquerda(atual)
        atual.chave = substituto.chave
        ch = substituto.chave
    
    if ch > atual.chave: return excluir_no(atual.dir, ch)
    return excluir_no(atual.esq, ch)

if __name__ == "__main__":
    raiz = No(15)
    nos = [No(12), 
    No(22), 
    No(10), 
    No(8), 
    No(12)]

    for no in nos:
        print("ITERAÇÃO COM NÓ DE CHAVE", no.chave)
        raiz = adicionar(raiz, no)

    print("Elemento 23", busca(raiz, 23))
    print("Elemento 22:", busca(raiz, 22))
    print("Quantidade de Nós:", n_nos(raiz))
    imprimir(raiz)
    print()
    pai, filho = busca_no_e_pai(raiz, 10)
    print("Pai:", pai, "| Filho:", filho)
    print("Remoção nó 9:", remove_no(raiz, 9))
    print("Remoção nó 10:", remove_no(raiz, 10))
    print(inserir_no(raiz, 88))
    em_nivel(raiz)