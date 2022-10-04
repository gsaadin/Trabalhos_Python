#Guilherme Saad Marino Botrel
#12121ECP018

#Primeiramente, valor de entrada será "captado" pelo comando input() na fomra de um número inteiro, associado a variável "s".
S = int(input(" Digite os segundos para a conversão: "))

#É feita uma verificação de entrada, conforme consta na especificação de entrada.
if S <= 10000000 and S >= 0:
 
#Dessa forma, serão feitas operações aritméticas para calcular os valores das variáveis "d", "h", "m", "r" e "s". 
#Sendo: d -> dias, h -> horas, m -> minutos, r -> resto, s -> segundos.

#Um dia tem 86400 segundos e é utilizado a divisão inteira pois o resto não é conveniente nessa operação específica, visto que dias são inteiros.
 D = S // 86400

#É preciso calcular o resto, com o fito de usa-lo nas operações seguintes.
 r = S % 86400

#Seguindo a mesma lógica do cálculo dos dias, a divisão inteira é usada junto ao resto para adquirirmos as horas e os minutos.
 H = r // 3600

#Um novo valor é atribuído a variável resto, para que o cálculo dos minutos e segundos sejam feitos.
 r = r % 3600
 M = r // 60

#Logo, é encontrado os segundos, provenientes do resto dos minutos.
 S = r % 60

#Por fim, os dados são impressos, conforme orientado na especificação de saída.
 print(D, "dia(s),", H, "hora(s),", M, "minuto(s) e", S, "segundo(s).")

#Uma mensagem é escrita orientando o usuário caso a condição não seja cumprida.
else: print("\nOs segundos devem estar contidos nesse intervalo: 0 ≤ N ≤ 10000000\nPor favor apresente um valor válido.")
