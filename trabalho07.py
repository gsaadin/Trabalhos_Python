#Guilherme Saad Botrel
#12121ECP018


def main():
    dna, primer, lig = input(), input(), []
    primer = troca(primer).upper()
    verificar(dna, primer, lig)
    cond(lig)


def cond(a):
    if a:
        for i in a:
            print("Ligacao na posicao {}".format(i))
    if not a:
        print("Nenhuma ligacao")


def verificar(a, b, c):
    for i in range(len(a) - len(b) + 1):
        if a[i:i + len(b)] == b:
            c.append(i)


def troca(a):
    a = a.strip("35")
    a = a[::-1]
    for i in range(len(a)):
        if a[i] == "A":
            a = a[:i] + "t" + a[i + 1:]
        if a[i] == "T":
            a = a[:i] + "a" + a[i + 1:]
        if a[i] == "C":
            a = a[:i] + "g" + a[i + 1:]
        if a[i] == "G":
            a = a[:i] + "c" + a[i + 1:]
    return a


main()
