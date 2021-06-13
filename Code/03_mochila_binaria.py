def maximiza_mochila(max, valor, peso, i):
    if i < 0: return 0
    if peso[i] < max:
        print('add', i)
        return maximiza_mochila(max-peso[i], valor, peso, i) + valor[i]
    return maximiza_mochila(max, valor, peso, i-1)

if __name__ == "__main__":
    maximo = 10
    itens = 4
    valor = [20,25,30,15]
    peso = [3,4,8,5]

    print(maximiza_mochila(maximo, valor, peso, itens-1))