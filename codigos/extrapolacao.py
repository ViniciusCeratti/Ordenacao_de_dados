def pesquisa_extrapolacao(lista, valor_busca):
    esquerda = 0
    direita = len(lista) - 1

    while esquerda <= direita and valor_busca >= lista[esquerda] and valor_busca <= lista[direita]:
        if esquerda == direita:
            if lista[esquerda] == valor_busca:
                return esquerda
            return -1

        posicao_estimada = esquerda + ((valor_busca - lista[esquerda]) * (direita - esquerda)) // (lista[direita] - lista[esquerda])

        if lista[posicao_estimada] == valor_busca:
            return posicao_estimada

        if lista[posicao_estimada] < valor_busca:
            esquerda = posicao_estimada + 1
        else:
            direita = posicao_estimada - 1

    return -1


# Exemplo de uso
lista = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

valor_busca = 12
indice = pesquisa_extrapolacao(lista, valor_busca)

if indice != -1:
    print("Elemento", valor_busca, "encontrado no índice", indice)
else:
    print("Elemento", valor_busca, "não encontrado.")