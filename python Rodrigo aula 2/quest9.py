n1 = int(input('Digite um número: '))
n2 = int(input('digite outro número: '))
n3 = int(input('digite mais um número: '))

if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n1 and n3 > n2:
    maior = n3

if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3

if n1 > n2 or n1 > n3:
    meio = n1
elif n2 > n1 or n2 > n3:
    meio = n2
elif n3 > n1 or n3 > n2:
    meio = n3

print(f'o maior número é {maior} o do meio é {meio} e o menor é {menor}')