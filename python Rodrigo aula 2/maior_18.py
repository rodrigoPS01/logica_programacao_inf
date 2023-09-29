nome = str(input('qual seu nome: '))
idade = int(input('qual sua idade: '))

if idade >= 18:
    print(f'{nome} você pode entrar ')
else:
    print(f'{nome} você é de menor e não pode entrar')
