POS_LETRA_Z = 90
POS_LETRA_A = 65
ALFABETO = 26

TEXTO = 'PENSAMENTO_COMPUTACIONAL'
print('Origial:', TEXTO)


SHIFT = 3
texto_cifrado = ''
for char in TEXTO:
    is_uppercase = POS_LETRA_A <= ord(char) <= POS_LETRA_Z
    if is_uppercase:
        shifted_char = chr(
            (ord(char) - POS_LETRA_A + SHIFT) % ALFABETO + POS_LETRA_A
        )
        texto_cifrado += shifted_char
    else:
        texto_cifrado += char

print('cifrado:',texto_cifrado)
