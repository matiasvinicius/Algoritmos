from queue import Queue

class No:
    def __init__(self, ch):
        self.esq = None
        self.dir = None
        self.chave = ch
        self.bal = 0
    
    def inserir(self, ch):
        if not(self): self = No(ch)
        
        elif ch < self.chave: 
            if not(self.esq): self.esq = No(ch)
            else: self.esq.inserir(ch)
        
        else: 
            if not(self.dir): self.dir = No(ch)
            else: self.dir.inserir(ch)

        return True

    def rotacao_direita(self):
        u = self.esq
        
        #LL
        if u.bal == -1:
            self.esq = u.dir
            u.dir = self
            self.bal = 0
            u.bal = 0 
            return u
        
        #LR
        elif u.bal == 1:
            v = u.dir
            u.dir = v.esq
            v.esq = u
            self.esq = v.dir
            v.dir = self
            if v.bal == -1: self.bal = 1
            else: self.bal = 0
            if v.bal == 1: u.bal = -1
            else: self.bal - 0
            v.bal = 0
            return v

        #Exclusão
        else:
            self.esq = u.dir
            u.dir = self
            u.bal = 1
            return u

    def rotacao_esquerda(self):
        u = self.esq
        
        #LL
        if u.bal == -1:
            self.esq = u.dir
            u.dir = self
            self.bal = 0
            u.bal = 0 
            return u
        
        #LR
        elif u.bal == 1:
            v = u.dir
            u.dir = v.esq
            v.esq = u
            self.esq = v.dir
            v.dir = self
            if v.bal == -1: self.bal = 1
            else: self.bal = 0
            if v.bal == 1: u.bal = -1
            else: self.bal - 0
            v.bal = 0
            return v

        #Exclusão
        else:
            self.esq = u.dir
            u.dir = self
            u.bal = 1
            return u
    
    def inserir_AVL(self, ch, alterou = False):
        if not(self): 
            self = No(ch)
            alterou = True
        
        elif ch < self.chave: 
            if not(self.esq): self.esq = No(ch)
            else: 
                self.esq.inserir_AVL(ch, alterou)
                if alterou:
                    alterou = False
                    if self.bal == 1: self.bal = 0
                    elif self.bal == 0: self.bal = -1
                    elif self.bal == -1: self.rotacao_esquerda()
        else: 
            if not(self.dir): self.dir = No(ch)
            else: 
                self.dir.inserir_AVL(ch, alterou)
                if alterou:
                    alterou = False
                    if self.bal == -1: self.bal = 0
                    elif self.bal == 0: self.bal = 1
                    elif self.bal == 1: self.rotacao_direita()

        return True

    def em_ordem(self):
        if self.esq: self.esq.em_ordem()
        print(self.chave)
        if self.dir: self.dir.em_ordem()

    def pre_ordem(self):
        print(self.chave)
        if self.esq: self.esq.pre_ordem()
        if self.dir: self.dir.pre_ordem()

    def pos_ordem(self):
        if self.esq: self.esq.pos_ordem()
        if self.dir: self.dir.pos_ordem()
        print(self.chave)

    def imprimir(self):
        print(self.chave, '(', end='')
        if self.esq: self.esq.imprimir() 
        if self.dir: self.dir.imprimir()
        print(')', end='')
    
    def em_nivel(self):
        if not(self): return
        q = Queue()
        q.put(self)
        while not(q.empty()):
            atual = q.get()
            print(atual.chave)
            if atual.esq: q.put(atual.esq)
            if atual.dir: q.put(atual.dir)

    def remover(self, ch):
        pai = substituto = pai_substituto = No
        no = self
        #Buscar nó com chave ch e seu pai
        while no:
            if no.chave == ch:
                break
            elif ch < no.chave:
                pai = no
                no = no.esq
            else:
                pai = no
                no = no.dir
        
        #Caso 1, não existe nó para ser removido
        if not(no): return False
        
        #Caso 2, nó a ser removido tem 1 ou nenhum filho
        if not(no.esq) or not(no.dir):
            if no.esq: substituto = no.esq
            else: substituto = no.dir

            #Se raíz
            if not(pai): self = substituto
            else:
                if pai.esq == no: pai.esq = substituto
                else: pai.dir = substituto

        #Caso 3, nó tem dois filhos
        else:
            #Procura o maior à esquerda e seu pai
            pai_substituto = no
            substituto = no.esq
            while substituto.dir:
                pai_substituto = substituto
                substituto = substituto.dir
            no.chave = substituto.chave
            if pai_substituto.esq == substituto:
                pai_substituto.esq = substituto.esq
            else:
                pai_substituto.dir = substituto.esq
            
        return True

if __name__ == "__main__":
    raiz = No(5)
    chaves = [1,2,3,4,6,7,8]

    for chave in chaves:
        raiz.inserir_AVL(chave)
    
    raiz.remover(2)

    raiz.em_nivel()
    print()
