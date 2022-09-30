# Guilherme Saad Botrel
# 12121ECP018

def main():
    matriz = []
    lista = []
    for i in range(10):  # Captando Matriz Grandona
        linha = [m for m in input().split()]
        matriz.append(linha)

    for k in range(len(matriz)):
        for j in range(len(matriz[0])):
            lista.append(matriz[k][j])

    ####
    palp = int(input())  # NÃºmeros de palpites
    chutes = []  # Lista dos palpites, ex: 'A'3, 'E'2, 'D'1...
    for i in range(palp):
        linha = [p for p in input().split()]
        chutes.append(linha)
        for a in range(len(chutes)):
            chutes[a][1] = int(chutes[a][1])


    indices = pos_to_value(chutes)
    confere(lista, indices)


###
def vale(X):
    alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    for k in range(len(alfabeto)):
        if alfabeto[k] == X:
            return k


###
def pos_to_value(pos):
    value = []
    for i in range(len(pos)):
        pos[i][0] = vale(pos[i][0])

    for j in range(len(pos)):
        Z = (pos[j][1] - 1) + (10 * pos[j][0])  # Ex E3 -> 4 + (10 * 3-1)
        value.append(Z)

    return value


###
def confere(li, ind):
    navios = []
    # Lista grandona
    # Indices dos chutes
    for p in range(len(li)):  # Procurando navios
        if li[p] != '.':
            navios.append(li[p])
    #print("navios:", navios)

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



if __name__ == '__main__':
    main()