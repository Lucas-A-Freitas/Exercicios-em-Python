# Receber uma texto do usuário, e e devolver o texto em caps lock, e mais pontos de exclamação concatenados ao texto.
# A quantidade de pontos de exclamação precisa ser do tamanho do texto.
texto = input("Digite algo: ").upper()
texto = texto + (len(texto) * str('!'))
print(texto)
