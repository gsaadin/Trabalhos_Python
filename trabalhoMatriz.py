# Guilherme Saad Botrel
# 12121ECP018

# Como padrao a funcao main sera definida.
def main():
    Mg = []
    Mp = []

# Legenda de variaveis:
# Mg -> Matriz grande
# Mp -> Matriz pequena
# Mgc -> Copia da matriz grande
# count -> Variavel acumulativa que conta os elementos similares.
# maior/ Max -> Maior numero de elementos similares.
# indices/ IJ -> Indices da posicao.
# similar = numero em decimais da razao de similares por total.

# Explicacao de raciocinio:
#   Usei 4 for principais. Os dois primeiros para comparar a matriz vertical e horizontalmente e as duas ultimas para
# comparar Mgc elemento por elemento com o Mp.
#   Basicamente, eu uso o fatiamento de listas para comparar seccao por seccao, com a matriz pequena. Logo dps disso, eu
# capto as posicoes do lugar com similaridade maxima e calculo a porcentagem da similaridade maxima.

    criar(Mg, Mp)  # Chamando funcao para criar as matrizes.

    Max, IJ = aaa(Mg, Mp)  # Max e IJ recebem o return da funcao.

    similar = Max / (len(Mp) ** 2)  # calculo para devolver a similaridade maxima.

    i, j = IJ  # i- linhas, j- colunas

    #printando saida.
    print("Posição: ({},{})".format(i, j))
    print("Similaridade máxima: {:.2f}%".format(similar * 100))  #:.f para duas casas decimais


def aaa(grande, pequeno): # funcao principal que percorre, fatia e compara as matrizes.
    indices = 0, 0
    count = 0
    maior = 0
    for i in range(len(grande) - len(pequeno) + 1):
        Mgc = grande[i:len(pequeno) + i]
        for j in range(len(grande[0]) - len(pequeno) + 1):

            for g in range(len(pequeno)):
                Mgc[g] = grande[i + g][j:len(pequeno[0]) + j]
                count = 0

            for p in range(len(pequeno)):
                for q in range(len(pequeno)):
                    if pequeno[p][q] == Mgc[p][q]:
                        count += 1
                        if count > maior:
                            maior = count
                            indices = i, j
    return maior, indices


def criar(x, y): # Funcao para criar as matrizes.
    big = int(input())

    for i in range(big):
        linha = [int(b) for b in input().split()]
        x.append(linha)

    small = int(input())

    for i in range(small):
        linha = [int(s) for s in input().split()]
        y.append(linha)


main()

# Fim!