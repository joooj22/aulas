print('O diretorio a seguir serve para o censo de 2025. Responda com s, n , numeros sem pontuacao ou como for pedido.')
idade = int(input('digite sua idade'))
if idade <0 or idade > 150:
    print('inválido, logo, reprovado.')
else:
    estudo = input('estuda?')
    trabalho = input('trabalha?')
    regime = input('em qual regime? responda com mei, estag ou outro')
    renda = int(input('Qual sua renda?'))
    aposentadoria = input('é aposentado?')
if regime == 'mei' and renda > '6750':
            print('reprovado.')
else:
            if regime == 'estag' and estudo == 'n':
                print('reprovado.')
            else:
                if aposentadoria == 's' and idade < '62': 
                    print('aprovado com ressalvas.')
                else:
                    if idade < 14 and estudo =='n':
                        print('aprovado com ressalvas.')
                    else:
                        if idade < 14 and trabalho == 's':
                            print('reprovado.')
                        else:
                            if idade >14 and idade <16 and trabalho == 's':
                                print('aprovado com ressalvas')
                            else:
                                print('aprovado!')








#opção 2 (ainda errado)
print('O diretorio a seguir serve para o censo de 2025. Responda com s, n , numeros sem pontuacao ou como for pedido.')
idade = int(input('digite sua idade'))
if idade <0 or idade > 150:
    print('inválido, logo, reprovado.')
else:
    estudo = input('estuda?')
    if estudo == 'n':
        trabalho = input('trabalha?')
        if trabalho == 's':
            regime = input('em qual regime? responda com mei, estag ou outro')
            renda = int(input('Qual sua renda?'))
        else:
           if trabalho == 'n':
            aposentadoria = input('é aposentado?')
           else:
              print('invalido.')
    else: 
        if regime == 'mei' and renda > 6750:
            print('reprovado')
        else:
            if aposentadoria == 's' and idade > 62:
                print('aprovado com ressalvas.')
            else:
                if idade < 14 and estudo == 'n':
                    print('aprovado com ressalvas.')
                else:
                    if idade < 14 and trabalho == 's':
                        print('reprovado.')
                    else:
                        if idade == 14 and trabalho == 's' and estudo == 's':
                            print('aprovado com ressalvas.')
                        else:
                            if idade == 15 and trabalho == 's' and estudo == 's':
                                print('aprovado com ressalvas.')
                            else:
                                if idade == 16 and trabalho == 's' and estudo == 's':
                                    print('aprovado com ressalvas.')
                                else:
                                    print('aprovado!')