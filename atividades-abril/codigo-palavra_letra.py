palavras = ["leet","code", "esperanca"]
x = "e"
criterio = []
for i in range(len(palavras)): 
    if x in palavras[i]:
        criterio.append(i)
    print(criterio)