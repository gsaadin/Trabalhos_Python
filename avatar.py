#Arthur Henrique Ferraz Netto
#Matrícula : 12121ECP019

#Entrada 
W = 0.0
F = 0.0
A = 0.0
E = 0.0
X = True

while(X == True): #Condição para o comando while ser realizado
    
    Y = input() #A variável Q recebe a letra digitada pelo jogador
    
    if (Y != "X"):
        
          P = float(int(input())) #A variável P recebe o valor de pontos digitada pelo jogador
        
          if (Y == "W"): #Water
             W = P + W
             F = F - P/2
             if F < 0:
                 F = float(0.0)

          if (Y == "F"): #Fire
             F = P + F
             W = W - P/2
             if W < 0:
                 W = float(0.0)

          if (Y == "A"): #Air
             A = P + A
             E = E - P/2
             if E < 0:
                 E = float(0.0)

          if (Y == "E"): #Earth
             E = P + E
             A = A - P/2
          if A < 0:
                 A = float(0.0)
                
    else:
        X = False #Caso o jogador digite a variável X o programa encerra o laço

#Saída
print("Pontuacao Final \nAgua: {}\nTerra: {}\nFogo: {}\nAr: {}".format(W, E, F, A))

if(W > 0 and F > 0 and A > 0 and E > 0):
        print("Treinamento realizado com sucesso.")
else:
        print("Realize mais treinamentos.")
        
            
        


