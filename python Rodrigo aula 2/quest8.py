p1 = float(input('qual o primeiro preço: '))
p2 = float(input('qual o segundo preço: '))
p3 = float(input('qual o treiceito preço: '))

if p1 < p2 and p1 < p3:
    print(f'compre o produto de valor {p1}')
elif p2 < p1 and p2 < p3:
    print(f'compre o produto de valor {p2}')
elif p3 < p1 and p3 < p2:
    print(f'compre o produto de valor {p3}')
else:
    print('existe produtos com mesmo valor')