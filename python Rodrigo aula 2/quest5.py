n1 = float(input('qual sua nota: '))
n2 = float(input('qual sua segunda nota: '))
s = (n1+n2)/2


if s == 10.0:
    print(f'{s} aprovado com distinção! ')
elif s < 7.0:
    print(f'{s} reprovado')
else:
    print(f'{s} aprovado')