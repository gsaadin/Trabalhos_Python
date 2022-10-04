# Guilherme Saad Marino Botrel
# 12121ECP018


W = float(0)
F = float(0)
E = float(0)
A = float(0)
X = 1

while X == 1:

    El = input()

    if El != "X":

        P = float(int(input()))

        if El == "W":
            W += P
            F -= P/2
            if F < 0:
                F = float(0)


        elif El == "F":
            F += P
            W -= P / 2
            if W < 0:
                W = float(0)

        elif El == "E":
            E += P                # Fogo x Água       Ar x Terra
            A -= P/2
            if A < 0:
                A = float(0)

        elif El == "A":
            A += P
            E -= P/2
            if E < 0:
                E = float(0)
    else:
        X = 0

print("Pontuacao Final\nAgua: {}\nTerra: {}\nFogo: {}\nAr: {}".format(W, E, F, A))

if A and E and W and F > 0:
    print("Treinamento realizado com sucesso.")

elif A or E or W or F == 0:
    print("Realize mais treinamentos.")
