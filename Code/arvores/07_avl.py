class No:
    def __init__(self, ch):
        self.esq = No
        self.dir = No
        self.chave = ch
    
    def inserir(self, ch):
        if self == No: 
            self = No(ch)
            return self
        
        elif ch < self.chave: 
            if self.esq == No: 
                self.esq = No(ch)
                return self
            else: self.esq = self.esq.inserir(ch)
        
        else: 
            if self.dir == No: 
                self.dir = No(ch)
                return self
            else: self.dir = self.dir.inserir(ch)

    
    def inserir_AVL(self, ch):
        if self == No: 
            self = No(ch)
            return self
        
        elif ch < self.chave: 
            if self.esq == No: 
                self.esq = No(ch)
                return self
            else: self.esq = self.esq.inserir(ch)
        
        else: 
            if self.dir == No: 
                self.dir = No(ch)
                return self
            else: self.dir = self.dir.inserir(ch)

    def em_ordem(self):
        if self.esq != No: self.esq.em_ordem()
        print(self.chave)
        if self.dir != No: self.dir.em_ordem()

    def maior_esquerdo(self, ch):
        pai = No
        maior_esq = self.esq
        while maior_esq != No:
            pai = maior_esq
            maior_esq = maior_esq.dir
        return pai, maior_esq

    def remover(self, ch):
        pai = substituto = pai_substituto = No
        no = self
        #Buscar nó com chave ch e seu pai
        while no != No:
            if no.chave == ch:
                break
            elif ch < no.chave:
                pai = no
                no = no.esq
            else:
                pai = no
                no = no.dir
        
        #Caso 1, não existe nó para ser removido
        if no == No: return False
        
        #Caso 2, nó a ser removido tem 1 ou nenhum filho
        if no.esq == No or no.dir == No:
            if no.esq != No:
                substituto = no.esq
            else:
                substituto = no.dir

            #Se raíz
            if pai == No:
                self = substituto
            else:
                if pai.esq == no: pai.esq = substituto
                else: pai.dir = substituto

        #Caso 3, nó tem dois filhos
        else:
            #Procura o maior à esquerda e seu pai
            pai_substituto = no
            substituto = no.esq
            while substituto.dir != No:
                pai_substituto = substituto
                substituto = substituto.dir
            no.chave = substituto.chave
            if pai_substituto.esq == substituto:
                pai_substituto.esq = substituto.esq
            else:
                pai_substituto.dir = substituto.esq
            

if __name__ == "__main__":
    raiz = No(20)
    nos = [12, 18, 28, 1, 21]

    for no in nos:
        raiz.inserir(no)
    
    raiz.em_ordem()
    print()
    raiz.remover(12)
    raiz.em_ordem()