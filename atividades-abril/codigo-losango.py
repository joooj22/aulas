losango = int(input('digite o valor inteiro e ímpar do losango. O numero sera a linha central.'))
tamanho = losango // 2 #quantas linhas vai ter além da central (7 mod 2 é 3, logo, linha central + 3 pra cima ou pra baixo(eu suponho))
if losango % 2 == 0:
    print('O número é invalido. Terminando operação.')
    exit()    #termina a operação caso o usuário nao coloque um número impar ("A verdadeira morte é a ignorância." Pitágoras)


for altura in range (tamanho+1):
    print('.' * (tamanho - altura)+ '*' * (2 * altura + 1)) 

for altura in range(tamanho):
    losango -= 2
    print('.' * (altura + 1) + '*' * losango)


#fim.