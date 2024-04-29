import random #colocar para poder utilizar random (ele da como 'nao declarado'caso nao tenha)
lista = []

for i in range(10): #10 fatores na lista
        lista.append(random.randint(1,100)) #numero aleatorio de cada fator entre 1 e 100

print ('lista antes:',lista)

n = len(lista)
for i in range(n):
        for j in range(n-1):
                if lista[j]>lista[j+1]:
                        temp = lista[j]
                        lista[j] = lista[j+1]
                        lista [j+1] = temp
#ordenando tudo dentro da lista

print ('lista depois',lista)

