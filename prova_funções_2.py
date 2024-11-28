#Crie uma função chamada maior_numero que receberá três números como argumentos.
#Esta função deve comparar os três números e identificar qual deles é o maior.
#Para isso, utilize uma estrutura de controle que verifique qual número é maior que os outros dois.
#A função deve então retornar o maior número encontrado.

def maior_numero(num1, num2, num3):
    return max(num1, num2, num3)

num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))
num3 = float(input('Digite o terceiro valor: '))

maior = maior_numero(num1, num2, num3)

print(f'O maior número é: {maior}')

