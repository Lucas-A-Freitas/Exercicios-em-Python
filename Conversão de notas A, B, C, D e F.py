nota = float(input('Digite sua nota de 0.00 até 10.00: '))
if nota < 6:
    print('F')
elif nota < 7:
    print('D')
elif nota < 8:
    print('C')
elif nota < 9:
    print('B')
elif nota < 10:
    print('A')
else:
    print('Nota invalida!')
