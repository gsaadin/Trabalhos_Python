# Guilherme Saad Botrel
# 1212ECP018


def main():  # Como ponto de partida, definimos a função main.
    n = int(input())  # N° de meses.
    D1 = 0   # Pessoas que (JA TOMARAM APENAS a primeira dose)
    sD2 = 0  # Soma das pessoas que (JA TOMARAM a primeira dose) ^ (JA TOMARAM a segunda dose).
    D1A = 0  # Pessoas que (JA TOMARAM a primeira dose) ^ (ESPERANDO a segunda dose COM atraso).
    D2A = 0  # Pessoas que (JA TOMARAM a primeira dose) ^ (JA TOMARAM a segunda dose COM atraso).
    j = 0    # Variável acumulativa para controle do While.
    
    # O inicio do codigo em si se da na criacao do laco de repeticao While, utilizarei ele para que a quantidade de vacinas por mes (vac), seja constantemente "resgatada".

    while j < n:

        vac = int(input())  # Vacinas por mes.

        j = j + 1

        # As condicoes dao inicio a realizacao das operacoes aritmeticas, que calcularao as saidas.
        if D1 == 0:
            D1 = vac

            if n == 1 and vac == 0:
                break
        # Após o D1 ser trabalhado, segui as ordens de prioridade da vacina, conforme consta no trabalho.
        # TABELA DE PRIORIDADES:
        # D1A -> D1 -> NOVAS PESSOAS "D0"

        else:
            if D1A > 0:
                if D1A == vac:
                    sD2 += D1A
                    D2A += D1A
                    D1A = 0
                    D1 = 0

                elif D1A < vac:
                    sD2 += D1A
                    D2A += D1A
                    D1 = diff(vac, D1A)
                    D1A = 0

                elif D1A > vac:
                    D1A = diff(D1A, vac)
                    D2A += vac
                    sD2 += vac
                    D1 = D1A

            else:
                if D1 == vac:
                    D2 = D1
                    sD2 += D2
                    D1 = 0

                elif D1 > vac:
                    D2 = vac
                    sD2 += D2
                    D1A = diff(D1, vac)

                elif D1 < vac:
                    D2 = D1
                    sD2 += D2
                    D1 = diff(vac, D1)
                    D1A = 0

    # As operacoes foram criadas na logica da prioridade vacinal, e notavel que apenas operacoes de subtracao e soma foram utilizadas.
    # A maioria das contas giram em torno de "transferencias" de vacinas, ou seja, assim que uma variavel ganha vacinas, outra deve perder.
    # Nem sempre isso acontece, como no caso em que sobram pessoas com apenas a primeira dose aplicada.
    # Ademais, as operacoes foram relizadas e agora aparecerao na saida do usuario.

    printar(sD2, D1, D2A, D1A)  # Função printar foi chamada apos o termino do While.


def printar(sD2, D1, D2A,D1A):  # Função printar criada essencialmente para facilitar a vizualizacao do que sera impresso.
    print("Pessoas completamente imunizadas:", sD2)
    print("Pessoas imunizadas apenas com uma dose:", D1)
    print("Pessoas que tomaram a segunda dose com atraso:", D2A)
    print("Pessoas esperando a segunda dose com atraso:", D1A)


def diff(a, b):  # Função diff foi criada pois não era viavel que o resultado das subtracoes fosse negativo.
    c = a - b
    if c < 0:
        return (-1) * c
    else:
        return c


main()  # No escopo Global, a funcao Main foi chamada para que o codigo se inicie.
# Fim.
