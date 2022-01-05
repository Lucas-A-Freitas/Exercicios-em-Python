# Como Unir e Separar Strings: join() e split()
lista = ['Brincando', 'Com', 'Strings']
# Unindo as palavras com vírgula
print(','.join(lista))
print(' '.join(lista))

# Usando Split()
texto = 'Brincando com strings'
print(texto.split())

# Vamos supor que alguem tenha nos dado a string: "123PI567PI9..."
# Fazendo: texto.split('PI')
# Ele vai arrancar os 'PI' da string e devolve uma lista com elementos separados onde antes era 'PI'.
texto1 = '123PI567PI9...'
print(texto1)
print(texto1.split('PI'))
