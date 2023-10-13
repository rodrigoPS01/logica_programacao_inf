while True:
    login = str(input('Digite seu login: '))
    senha = str(input('Digite sua senha: '))
    if login != senha:
        print('usuario e senha valido')
        break
    elif login == senha:
        print('usuario e senha invalido ')