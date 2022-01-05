# Buscar e Substituir substring em String
# Usamos o método endswith() (do inglês 'termina com' ) para localizar uma substring;
# (passada como argumento para o método) dentro de uma string maior, da seguinte maneira:
# texto.endswith(substring)
# Se a string substring estiver ao final da string texto, esse método retorna True.
# Por exemplo, vamos criar um script que pede ao usuário o nome e extensão de um arquivo.
# Se terminar com .txt, .pdf ou .png, dizemos se é um arquivo de texto, um PDF ou uma imagem.
# EXEMPLO:
texto = input('Digite o nome do arquivo e sua extensão: ').upper()
if texto.endswith(".PDF"):
    print('É um arquivo do Acrobat Reader')
elif texto.endswith(".TXT"):
    print('É um arquivo de texto')
elif texto.endswith(".PNG"):
    print('É uma imagem')
else:
    print('É outro tipo de arquivo')

# A função .startswith() é usada para procurar determinado valor no inicio da string, retornando TRUE caso encontrado
print('Procurando a palavra "Brincando" no começo do texto com .startwith()')
texto1 = 'Brincando com string'
print(texto1.startswith('Brincando'))
print(texto1.startswith('Com'))

# Achar o que quiser em qualquer lugar de uma string: find()
lista = str(('Francisco', 'Pedro', 'Lucas', 'Gabriel'))
print(lista.find('Francisco'))
print(lista.find('Pedro'))
print(lista.find('Lucas'))
print(lista.find('Gabriel'))
print(lista.find('Casimiro'))

# Usando replace() para substituir na string

texto2 = 'A palavra "Python" sera substituida'
print(texto2.replace('Python', 'C#'))
