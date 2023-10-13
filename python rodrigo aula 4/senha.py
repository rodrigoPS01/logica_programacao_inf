while True:
    senha = str(input('Digite uma senha: '))
    Tem_letra = False
    Tem_numero = False
    for letra in senha:
        if letra in ('0123456789'):
            Tem_numero = True
        elif letra in ('ABCDEFGHIJKLMNOPQRSTUVWXYZabacdefghijklmnopqrstuvwxyz'):
            Tem_letra = True
    if len (senha) > 8 and Tem_numero == True and Tem_letra == True:
        print('Senha valida')
        break
    else:
        print('Senha invalida')