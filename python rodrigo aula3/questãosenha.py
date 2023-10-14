senha = str(input('Digite uma senha: '))
letra_maiuscula = False
letra_minuscula = False
numero = False
especial = False
for letra in senha:
    if letra in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        letra_maiuscula = True
    elif letra in ('abcdefghijklmnopqrstuvwxyz'):
        letra_minuscula = True
    elif letra in ('0123456789'):
        numero = True
    else:
        especial = True

if letra_maiuscula == True and letra_minuscula == True and numero == True and especial == True:
    print('Senha valida :D')
else:
    print('Senha invalida ')