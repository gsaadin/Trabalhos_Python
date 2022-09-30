def main():
    n = [int(i) for i in input().split()]
    k = 1
    x = 0
    for j in range(0, len(n)):
        if k < len(n):
            for i in range(0, len(n)):
                if n[j] < n[k]:
                    x += 1
            if n[j] >= n[k]:
                roletar(n)
                x = 0
            k += 1
    if x == 0 or x == 21:
        print("Senha incorreta")
    else:
        print("Klift, Kloft, Still, a porta se abriu")


def roletar(n):
    n.append(n[0])
    del (n[0])
    return n

main()
