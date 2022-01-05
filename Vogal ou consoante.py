#Programa que verifique se uma letra digitada é vogal ou consoante.
char = input('Digite um caractere: ').lower()
if char.isnumeric():
    print('Digite somente letras!')
elif char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
    print('Vogal')
else:
    print('Consoante')
