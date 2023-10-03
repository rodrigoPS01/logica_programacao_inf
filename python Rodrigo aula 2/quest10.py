nome = str(input('Qual é o seu nome? '))
turno = str(input('Qual é o seu turno?[M|T|N] '))

if turno in ('Mm'):
    print(f'Bom dia, {nome}')
elif turno in ('Tt'):
    print(f'Boa tarde, {nome}')
elif turno in ('Nn'):
    print(f'Boa noite, {nome}')
else:
    print(f'{nome}, digite uma opção valida de turno com M para manhã, T para tarde e N para noite')