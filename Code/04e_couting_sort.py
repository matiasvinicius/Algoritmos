def couting_sort(A, k):
    n = len(A)
    ordenado = [None] * n
    quantidade = [0] * k

    for j in range(n): 
        quantidade[A[j]] += 1
    for i in range(1, k): 
        quantidade[i] += quantidade[i-1]
    for j in reversed(range(0, n)):
        ordenado[quantidade[A[j]]-1] = A[j]
        quantidade[A[j]] -= 1

    return ordenado


if __name__ == "__main__":
    A = [8,4,4,1,5,2,7,6]
    k = 9
    print(couting_sort(A, k))