import math

def jump_search(lista, valor_busca):
    tamanho = len(lista)
    step = int(math.sqrt(tamanho))
    anterior = 0

    while lista[min(step, tamanho) - 1] < valor_busca:
        anterior = step
        step += int(math.sqrt(tamanho))
        if anterior >= tamanho:
            return -1

    while lista[anterior] < valor_busca:
        anterior += 1
        if anterior == min(step, tamanho):
            return -1

    if lista[anterior] == valor_busca:
        return anterior

    return -1


# Exemplo de uso
lista = [1, 4, 7, 10, 15, 18, 20, 23, 30, 35]

valor_busca = 15
indice = jump_search(lista, valor_busca)

if indice != -1:
    print("Elemento", valor_busca, "encontrado no índice", indice)
else:
    print("Elemento", valor_busca, "não encontrado.")