def busca_binaria(A, valor, n):
    ini = 0
    fim = n-1

    while ini <= fim:
        meio = int((ini+fim)/2)
        print(meio)
        if valor > A[meio]: ini = meio+1
        elif valor < [meio]: fim = meio-1
        else: return meio
    
    return -1



if __name__ == "__main__":
    A = [6,2,3,4,5,6]
    A = sorted(A)
    valor = 6
    print(A)
    print(busca_binaria(A, 5, len(A)))