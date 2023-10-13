import random

nomes = []
tels = []
ends = []

while True:
    nome = str(input("Coloque o nome do cliente: "))
    print(nome)
    if nome == "fim":
        break
    tel = str(input("Coloque o telefone do cliente: "))
    print(tel)

    end = str(input("Coloque o endereço do cliente: "))
    print(end)
   

    nomes.append(nome)
    tels.append(tel)
    ends.append(end)

initializing nomes
radom.choice()


