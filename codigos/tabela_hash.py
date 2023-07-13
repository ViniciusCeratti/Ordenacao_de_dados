class TabelaHash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]

    def calcular_hash(self, chave):
        return hash(chave) % self.tamanho

    def inserir(self, chave, valor):
        indice = self.calcular_hash(chave)
        self.tabela[indice].append((chave, valor))

    def buscar(self, chave):
        indice = self.calcular_hash(chave)
        lista = self.tabela[indice]

        for item in lista:
            if item[0] == chave:
                return item[1]

        return None


# Exemplo de uso
tabela = TabelaHash(10)

# Inserindo elementos na tabela hash
tabela.inserir('97', 'a')
tabela.inserir('98', 'b')
tabela.inserir('99', 'c')
tabela.inserir('100', 'd')
tabela.inserir('101', 'e')
tabela.inserir('102', 'f')
tabela.inserir('103', 'g')
tabela.inserir('104', 'h')
tabela.inserir('105', 'i')
tabela.inserir('106', 'j')
tabela.inserir('107', 'k')
tabela.inserir('108', 'l')
tabela.inserir('109', 'm')
tabela.inserir('110', 'n')
tabela.inserir('111', 'o')
tabela.inserir('112', 'p')
tabela.inserir('113', 'q')
tabela.inserir('114', 'r')
tabela.inserir('115', 's')
tabela.inserir('116', 't')
tabela.inserir('117', 'u')
tabela.inserir('118', 'v')
tabela.inserir('119', 'w')
tabela.inserir('120', 'x')
tabela.inserir('121', 'y')
tabela.inserir('122', 'z')

# Buscando elementos na tabela hash
print(tabela.buscar("100"))  # Saída: valor1
print(tabela.buscar("111"))  # Saída: valor2
