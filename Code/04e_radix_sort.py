def couting_sort_str(A, indice, k):
    n = len(A)
    ordenado = [''] * n
    quantidade = [0] * k

    for j in range(n): 
        quantidade[ord(A[j][indice])] += 1
    for i in range(1, k): 
        quantidade[i] += quantidade[i-1]
    for j in reversed(range(0, n)):
        ordenado[quantidade[ord(A[j][indice])]-1] = A[j]
        quantidade[ord(A[j][indice])] -= 1
    return ordenado

def radix_sort(A, n_digitos):
    n_unicode = 256
    for i in reversed(range(n_digitos)):
        A = couting_sort_str(A, i, n_unicode)
        print(A)
    return 0

if __name__ == "__main__":
    A = ['abcd', 'bcda', 'abcd', 'poxa', 'poze', 'vida', 'rodo', 'xypc']
    n_digitos = 4
    radix_sort(A, n_digitos)