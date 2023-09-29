n1 = int(input('Digite um número: '))
n2 = int(input('digite outro número: '))
n3 = int(input('digite mais um número: '))

if n1 > n2 and n1 > n3:
    print(f'o número {n1} é maior que {n2} e {n3}')
elif n2 > n1 and n2 > n3:
    print(f'o número {n2} é maior que {n1} e {n3}')
elif n3 > n2 and n3 > n1:
    print(f'o número {n3} é maior que {n1} e {n2}')
else:
    print('possui números com igual valor')