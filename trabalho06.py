#Guilherme Saad Botrel
#12121ECP018

# Como padrao a funcao main sera definida.
def main():
    n = int(input())
    cap = int(input())
    lpeso = [int(input()) for peso in range(n)]
    lvalor = [int(input()) for valor in range(n)]
    razao = [lvalor[r] / lpeso[r] for r in range(n)]
    mochilaP = []
    mochilaV = []

    while razao:
        if cap >= lpeso[ImaiorR(razao)]:  # Se couber:
            
            mochilaP.append(lpeso[ImaiorR(razao)])  # Adiciono o peso do objeto com a maior razao a mochilaP
            mochilaV.append(lvalor[ImaiorR(razao)])  # Adiciono o valor do objeto com a maior razao a mochilaV
            
            cap = cap - mochilaP[-1]  # Mochila perde capacidade a medida em que entram objetos
            
            del (lpeso[ImaiorR(razao)])  # Deleto o peso do objeto com a maior razao
            del (lvalor[ImaiorR(razao)])  # Deleto o valor do objeto com a maior razao
            del (razao[ImaiorR(razao)])  # Deleto a maior razao

        if not razao:
            break

        if cap < lpeso[ImaiorR(razao)]:  # Se NAO couber:
            
            del (lpeso[ImaiorR(razao)])  # Deleto o peso do objeto com a maior razao
            del (lvalor[ImaiorR(razao)])  # Deleto o valor do objeto com a maior razao
            del (razao[ImaiorR(razao)])  # Deleto a maior razao

    print(somatorio(mochilaV))  # A saida e o somatorio do valor dos intens que entraram na mochila de valores.
    print(somatorio(mochilaP))  # A saida e o somatorio do peso dos intens que entraram na mochila de pesos.

def Max(n):
    Max = n[0]
    for i in n:
        if i > Max:
            Max = i
    return Max

def somatorio(n):
    som = 0
    for i in n:
        som += i
    return som

def ImaiorR(razao):
    return razao.index(Max(razao))

main()

