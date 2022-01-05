# Transformando strings em maiúscula e minúscula
# .upper() e .lower()
# O .Upper() recebe o valor de uma string e retorna a mesma em maiúscula
# Exemplo:
texto = 'brincando com strings'
print(texto)
texto = texto.upper()
print(texto)
# Ou
print(texto.upper())

# A mesma coisa com minúsculo, usando o .lower()
texto2 = 'TEXTO EM MINÚSCULO'
print(texto)
texto2 = texto2.lower()
# Ou
print(texto2.lower())

# A função .islower() verifica se o texto é minúsculo, se for, retorna TRUE, se não retorna FALSE

texto3 = 'TEXTO EM MAIÚSCULO'
print(texto3)
print(texto3.islower())
print('Observe que o texto foi escrito em maiúsculo, logo o retorno foi FALSE')
texto4 = 'texto em minúsculo'
print(texto4)
print(texto4.islower())
print('Agora ele retorna o TRUE, por que o texto estava em minúsculo')

# A função .isupper() verifica se o texto é maiúsculo, se for, retorna TRUE, se não retorna FALSE

texto5 = 'texto em minúsculo'
print(texto5)
print(texto5.isupper())
print('Observe que o texto foi escrito em minúsculo, logo o retorno foi FALSE')
texto6 = 'TEXTO EM MAIÚSCULO'
print(texto6)
print(texto6.isupper())
print('Agora ele retorna o TRUE, por que o texto estava em maiúsculo')
