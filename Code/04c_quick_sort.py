def particao(A, ini, fim):
    pivo = A[fim]
    i = ini
    j = fim - 1

    while i <= j:
        if A[i] <= pivo:
            i += 1
        elif A[j] > pivo:
            j -= 1
        else:
            aux = A[i]
            A[i] = A[j]
            A[j] = aux
            i += 1
            j -= 1
    
    A[fim] = A[i]
    A[i] = pivo
    return i

def quick_sort(A, ini, fim):
    if ini < fim:
        p = particao(A, ini, fim)
        quick_sort(A, ini, p-1)
        quick_sort(A, p+1, fim)
    return A

if __name__ == "__main__":
    A = [4,4,52,-6,2,20]
    print(quick_sort(A, 0, len(A)-1))