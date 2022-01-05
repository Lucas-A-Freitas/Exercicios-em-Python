# Você criou um software na sua escola, onde você pergunta a opinião dos alunos sobre a linguagem de programação;
# Python e tem que apresentar esse texto pro dono da escola.
# Porém, os alunos escrevem muito 'Pyton' ao invés de 'Python'. E também usam muito 'eh' ao invés de 'é'.

texto = str(input('O que está achando do curso de Python?'))
texto = texto.replace('pyton', 'python')
texto = texto.replace('eh', 'é')
print('Texto corrigido: {}'.format(texto))
