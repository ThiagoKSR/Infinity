# Crie um programa em Python para verificar se um número é positivo, negativo ou zero. 
# O programa deve solicitar ao usuário que insira um número e, em seguida, imprimir uma mensagem indicando a natureza do número.
# Se o número for maior que zero, exiba a mensagem "O número é positivo." 
# Se for menor que zero, exiba "O número é negativo." Caso seja zero, a mensagem deve ser "O número é zero."
# Utilize estruturas condicionais e formatação com F-string para criar o programa de forma clara.
print('Olá. Vamos verificar a natureza do número escolhido? ')
numero = float(input('Digite um número para verificar sua natureza: '))
if numero < 0:
    print(f'O número {numero} é negativo.')
elif numero > 0:
    print(f'O número {numero} é positivo.')
else:
    print('O número é zero.')