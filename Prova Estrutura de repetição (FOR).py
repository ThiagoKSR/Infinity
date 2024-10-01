# Você está desenvolvendo um programa em Python para calcular a soma dos números pares dentro de um intervalo determinado pelo usuário. 
# O programa deve solicitar ao usuário que insira dois números inteiros, representando o início e o fim do intervalo (inclusive).
# Utilize um loop 'for' para iterar sobre todos os números no intervalo e somar apenas os números pares. 
# Implemente a estrutura 'else' para exibir uma mensagem indicando que não há números pares no intervalo, caso seja o caso.
# Ao final, exiba a soma dos números pares encontrados.
numeros_somados = 0
numeros_pares = 0

print('-='*50)
numero_1 = int(input('Digite um valor inteiro para o INÍCIO do intervalo: '))
numero_2 = int(input('Digite outro valor inteiro para o FIM do intervalo: '))
print('-='*50)

for c in range(numero_1, numero_2 +1):
    if c %2 == 0:
        numeros_pares += c
        numeros_somados += c %2 == 0

if numeros_pares > 0:
    print(f'A soma dos números pares é: {numeros_pares}')
    print(f'Foram somados: {numeros_somados} números entre {numero_1} e {numero_2} ')
    
else:
    print('Não há numeros pares.')