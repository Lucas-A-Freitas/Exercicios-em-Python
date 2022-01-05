# Faça um Programa que leia três números e mostre-os em ordem decrescente.
num1 = int(input("Digite um numero inteiro:"))
num2 = int(input("Digite aqui outro numero inteiro:"))
num3 = int(input("Digite o terceiro numeo inteiro:"))
print(num1, '-', num2, '-', num3)
if num3 > num2:
    aux = num3
    num3 = num2
    num2 = aux
if num2 > num1:
    aux = num2
    num2 = num1
    num1 = aux
if num3 > num2:
    aux = num3
    num3 = num2
    num2 = aux
print(num1, '-', num2, '-', num3)
