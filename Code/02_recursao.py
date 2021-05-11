def busca_binaria(A, valor, n):
    ini = 0
    fim = n-1

    while ini <= fim:
        meio = int((ini+fim)/2)
        if valor > A[meio]: ini = meio+1
        elif valor < A[meio]: fim = meio-1
        else: return meio
    return -1

def busca_binaria_rec(A, valor, ini, fim):
    if fim <= ini: return -1
    meio = int((ini+fim)/2)
    if valor > A[meio]: ,
        return busca_binaria_rec(A, valor, meio+1, fim)
    elif valor < A[meio]: 
        return busca_binaria_rec(A, valor, ini, meio-1)
    else: 
        return meio

if __name__ == "__main__":
    A = [6,2,3,4,5,6]
    A = sorted(A)
    valor = 5
    print("Buscar em ", A, "o valor ", valor)
    print(busca_binaria_rec(A, valor, 0, len(A)))