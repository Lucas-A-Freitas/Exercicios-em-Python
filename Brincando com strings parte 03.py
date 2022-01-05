# Vamos ver mais algumas funções para usar com strings!
# A primeira dela é a isalpha(), ela serve para verificar se o texto digitado é somente letras, retornando TRUE caso
# seja verdade, ou FALSE se tiver outros caracteres no texto alem das letras
texto = str(input('Digite algo aqui: '))

if texto.isalpha():
    print('Tudo letra')
else:
    print('Tem algo a mais que letra ai meu parceiro')

# Já o isdecimal() serve para testar se é tudo números:
numero = input('Digite algo aqui: ')

if numero.isdecimal():
    print('Tudo número')
elif numero.isalpha():
    print('Tudo letra')
else:
    print('Tudo misturado, vazio ou caractere especial')

# A função isalnum() serve para saber se tem somente letra e números:
numero2 = input('Digite algo aqui: ')

if numero2.isdecimal():
    print('Tudo número')
elif numero2.isalpha():
    print('Tudo letra')
elif numero2.isalnum():
    print('Letras e números')
else:
    print('Vazio ou caractere especial')

# Já o método isspace() só retorna True se tivermos espaço em branco, tabulação ou quebra de linha.
texto = input("Digite uma string: ")

if numero2.isdecimal():
    print('Tudo número')
elif numero2.isalpha():
    print('Tudo letra')
elif numero2.isalnum():
    print('Letras e números')
elif numero2.isspace():
    print('Composto somente por espaço, tabulação ou quebra de linha')
else:
    print('Caractere especial')
