# Guilherme Saad Botrel
# 12121ECP018

# Legenda de variaveis:
# matriz = Nosso mar, matriz 10x10 dos pontos e navios.
# lista = A matriz 10x10 em forma de lista, uma matriz 1x100, do mesmo mar.
# palp = Numero de palpites.
# chutes = Palpites armazenados em listas de coordenadas ['Letra', Número].
# indices = posicao dos palpites na matriz 1x100.
# navios = Lista que guardam Navios represetados por Letras.

# Explicação do raciocínio:
#   A ideia principal e apenas transformar a matriz em uma lista, tendo em vista que o "campo de batalha naval" tem
# sempre o mesmo tamanho. Desse modo, a verificacao de correspondencia ocorrera de maneira mais simples.
#   Essa forma de solucao tem dois problemas, sendo a primeira a transformacao das coordenadas, ex: A5, H8, J10, em
# indices das posicoes da matriz 1x100.
#   Resolvi essa questao elaborando uma formula: {"M"X = (X-1) + K*m} -> "M"X e a coordenada, X e o numero que indica
# as colunas, "M" e a letra que representa as linhas, m e o numero que representa a letra ex: A-0, B-1, C-2, por fim,
# K e uma constante, no nosso caso o 10.
#   O segundo problema foi na parte de afundar o Navio. Precisei criar uma lista de navios representados por tudo
# diferente de '.' que existem no nosso mar, ao mesmo tempo em que quando eu acertasse um navio, a letra do navio
# ficasse minuscula, logo, se houver apenas letras minusculas do determinado navio na lista, quer dizer que ele afundou.

def main():
    matriz = []
    lista = []
    for i in range(10):  # Captando Matriz 10x10
        linha = [m for m in input().split()]
        matriz.append(linha)

    for k in range(len(matriz)):
        for j in range(len(matriz[0])):
            lista.append(matriz[k][j])

    palp = int(input())
    chutes = []
    for i in range(palp):
        linha = [p for p in input().split()]
        chutes.append(linha)
        for a in range(len(chutes)):  # Captando listas de palpites e mudando para inteiro os numeros.
            chutes[a][1] = int(chutes[a][1])

    indices = pos_to_value(chutes)
    confere(lista, indices)


## Funcao que retorna o valor de cada letra para aplicar na formula.
def vale(X):
    alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    for k in range(len(alfabeto)):
        if alfabeto[k] == X:
            return k


## Funcao que retorna o indice da matriz 1x100.
def pos_to_value(pos):
    value = []
    for i in range(len(pos)):
        pos[i][0] = vale(pos[i][0])

    for j in range(len(pos)):
        Z = (pos[j][1] - 1) + (10 * pos[j][0])  # Ex E3 -> 4 + (10 * 3-1)
        value.append(Z)

    return value


## Funcao principal que confere se o palpite foi certo, além de verificar se afunda ou nao.
def confere(li, ind):
    navios = []
    # Lista grandona
    # Indices dos chutes
    for p in range(len(li)):  # Procurando navios
        if li[p] != '.':
            navios.append(li[p])

    for i in range(len(ind)):  # Acertando navios
        if li[ind[i]] != '.':

            var = li[ind[i]]
            li[ind[i]] = li[ind[i]].lower()

            navios.remove(var)
            navios.append(var.lower())

            if var in navios:
                print("atingiu o navio", var.upper())
            if var not in navios:
                print("afundou o navio", var.upper())

        else:
            print("agua")


if __name__ == '__main__':  # Verificando se esta sendo executado como script.
    main()

# Fim!
