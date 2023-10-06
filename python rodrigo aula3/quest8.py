palavra = str(input('Escreva uma palavra: '))
quantia = 0
for letra in palavra:
    if letra in 'aeiouAEIOU':
        quantia = quantia + 1

print(f'Sua palavra {palavra} tem {quantia} vogais.')