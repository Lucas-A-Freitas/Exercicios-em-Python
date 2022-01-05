print('1. Idoso')
print('2. Gestante')
print('3. Cadeirante')
resposta = int(input('Digite o número no qual você se encaixa: '))
if (resposta==1) or (resposta==2) or (resposta==3):
    print('Você tem direito a fila preferencial!')
else:
    print('Você não tem direito a fila preferencial!')