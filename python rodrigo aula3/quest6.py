numero = int(input('Qual o seu númeor: '))
n_primo = True
for x in range(2,numero):
    if numero % int(x) == 0:
        n_primo = False
    
if n_primo == False:
    print('O seu número não é primo')
else:
    print('O seu número é primo')
