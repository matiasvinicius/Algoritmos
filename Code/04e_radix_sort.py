def couting_sort(A, indice, k):
    n = len(A)
    ordenado = [''] * n
    quantidade = [0] * k

    for j in range(n): 
        quantidade[int(A[j][indice])] += 1
    for i in range(1, k): 
        quantidade[i] += quantidade[i-1]
    for j in reversed(range(0, n)):
        ordenado[quantidade[int(A[j][indice])]-1] = A[j]
        quantidade[int(A[j][indice])] -= 1
    return ordenado

def radix_sort(A, n_digitos):
    for i in reversed(range(n_digitos)):
        A = couting_sort(A, i, 10)
        print(A)
    return 0

if __name__ == "__main__":
    A = ['12','20','56','13','18','15','30','31','20','49']
    n_digitos = 2
    radix_sort(A, n_digitos)