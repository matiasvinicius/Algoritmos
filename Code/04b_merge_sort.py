def merge(esq, dir):
    i, j = 0, 0
    ordenados = list()

    while i < len(esq) and j < len(dir):
        if esq[i] <= dir[j]:
            ordenados.append(esq[i])
            i += 1
        else:
            ordenados.append(dir[j])
            j += 1
    
    if i < len(esq):
        ordenados += esq[i:]
    
    elif j < len(dir):
        ordenados += dir[j:]
    
    return ordenados
        
def merge_sort(A):
    if len(A) > 1:
        meio = len(A) // 2
        esq = merge_sort(A[:meio])
        dir = merge_sort(A[meio:])
        A = merge(esq, dir)
    return A

if __name__ == "__main__":
    A = [4,4,52,-6,2,20]
    print(merge_sort(A))