"""
A = uma lista
i_pai = índice do "nó" pai (posição no arranjo)
n_heap = comprimento da lista
Verifica se o nó pai é maior que os filhos (esq e dir)
Se for menor, realiza a troca e chama recursivamente para o novo pai
"""
def refazer_heap_max(A, i_pai, n_heap):
    esq = 2*i_pai + 1 
    dir = 2*i_pai + 2

    if esq < n_heap and A[esq] > A[i_pai]:
        maior = esq
    else:
        maior = i_pai
    
    if dir < n_heap and A[dir] > A[maior]:
        maior = dir
    
    if maior != i_pai:
        aux = A[maior]
        A[maior] = A[i_pai]
        A[i_pai] = aux
        refazer_heap_max(A, maior, n_heap)

def construir_heap_max(A):
    n_heap = len(A)
    i = (n_heap // 2) - 1
    while i >= 0:
        refazer_heap_max(A, i, n_heap)
        i -= 1

def heap_sort(A):
    construir_heap_max(A)
    n_heap = len(A)
    i = len(A) - 1
    while i > 0:
        aux = A[0]
        A[0] = A[i]
        A[i] = aux
        n_heap -= 1
        i -= 1
        refazer_heap_max(A, 0, n_heap)

if __name__ == "__main__":
    A = [12,5,9,3,14,0,-6,5,17,13,3,50]
    heap_sort(A)
    print(A)