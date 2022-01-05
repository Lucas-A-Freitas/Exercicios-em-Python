# Crie um script que peça uma string ao usuário e diga se:
# Ela é toda maiúscula
# Ela é toda minúscula
# Tem caracteres maiúsculos e minúsculos
texto = str(input('Digite algo: '))
if texto.isupper():
    print('Tudo em maiúsculo!')
elif texto.islower():
    print('Tudo em minúsculo!')
else:
    print('Texto misturado')
    