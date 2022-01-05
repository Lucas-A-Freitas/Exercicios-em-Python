# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
resposta = input(print('Em qual turno você estuda? M - matutino, V - vespertino ou N - Nortuno')).upper()
if resposta == 'M':
    print('Bom dia')
elif resposta == 'V':
    print('Boa tarde')
elif resposta == 'N':
    print('Boa noite')
else:
    print('Valor inválido')
