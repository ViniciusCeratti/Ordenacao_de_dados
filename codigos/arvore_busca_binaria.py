class No:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave):
        if self.raiz is None:
            self.raiz = No(chave)
        else:
            self._inserir_recursivo(chave, self.raiz)

    def _inserir_recursivo(self, chave, no):
        if chave < no.chave:
            if no.esquerda is None:
                no.esquerda = No(chave)
            else:
                self._inserir_recursivo(chave, no.esquerda)
        else:
            if no.direita is None:
                no.direita = No(chave)
            else:
                self._inserir_recursivo(chave, no.direita)

    def buscar(self, chave):
        return self._buscar_recursivo(chave, self.raiz)

    def _buscar_recursivo(self, chave, no):
        if no is None or no.chave == chave:
            return no

        if chave < no.chave:
            return self._buscar_recursivo(chave, no.esquerda)
        else:
            return self._buscar_recursivo(chave, no.direita)


# Exemplo de uso
arvore = ArvoreBinariaBusca()

# Inserindo elementos na árvore
arvore.inserir(8)
arvore.inserir(3)
arvore.inserir(10)
arvore.inserir(1)
arvore.inserir(6)
arvore.inserir(14)
arvore.inserir(4)
arvore.inserir(7)
arvore.inserir(13)

# Buscando elementos na árvore
no_encontrado = arvore.buscar(6)
if no_encontrado:
    print("Elemento encontrado:", no_encontrado.chave)
else:
    print("Elemento não encontrado.")