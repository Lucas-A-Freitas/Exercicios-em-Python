# Faça um programa que pede dois inteiro e armazene em duas variáveis.
# Em seguida, troque o valor das variáveis e exiba na tela
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
print('Primeiro número: ', n1)
print('Segundo número: ', n2)
print('Invertendo... aguarde...')
aux = n2
n2 = n1
n1 = aux
print('Primeiro número, ', n1)
print('Segundo número, ', n2)
