ano = int(input('digite o ano'))
if ano % 4 == 0:
        print('é um ano bissexto')
else:
        ano = ano + (4 - ano % 4)
        print('não é um ano bissexto, o próximo sera',ano)
