while True:
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    salario = float(input('Digite seu salario: '))
    sexo = str(input('Qual o seu sexo? [F|M]'))
    estado = str(input('Qual o seu estado civil: [s | c | v | d]'))

    if len(nome) > 3 and idade in range(0,151) and salario > 0 and estado in ('scvdSCVD'):
        print('As condições são atendidas :D ')
        break
    else:
        print('Alguma condição não é valida ')