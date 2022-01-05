# Aqui brinquei um pouco com strings
print('Barra dupla serve para mostrar um unica barra na string')
print('Exemplo: \\')

print('Uma barra com uma aspa simples, serve para exibir uma aspa simples')
print('Exemplo: \'')

print('Uma barra com uma aspa dupla, serve para exibir uma aspa dupla')
print('Exemplo: \"')

print('Barra seguido pela letra "a" serve para dar um bipe (?)')
print('Exemplo: \a')

print('Barra seguida pela letra "b" serve para apagar o ultimo caractere anterior ao comando')
print('Exemplo: irei digitar oi, mas veja o que aparece: oi\b, viu? olhe no código que entedera ;)')

print('A barra + a letra "n" é utilizada para pular uma linha no meio do texto')
print('Observe que a partir da qui.. \neste texto continua na linha de baixo ')

print('A barra + a letra "t" serve para dar um espaço equivalente ao tab')
print('\t Exemplo')

# Usando a função len() para descobrir o tamanho de texto (incluindo espaços)
texto = 'Ola, vamos brincar com strings?'
print('O texto tem {} letras'.format(len(texto)))

# Concatenando strings usando o operador +
texto = "Brincando"
print(texto)
texto = texto + " com strings"
print(texto)
