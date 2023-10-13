while True:
    nota = float(input('digite sua nota: '))

    if nota >= 0 and nota <= 10:
        print('Nota valida ')
        break
    else:
        print('Nota invalida ')