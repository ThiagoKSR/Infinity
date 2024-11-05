# idade = int(input('Digite sua idade: '))
# if idade < 12:
#     print('Classificação criança.')
# elif idade >= 12 and idade <= 17:
#     print('Classificação: Adolescente.')
# elif idade >= 18 and idade <= 59:
#     print('Classificação: Adulto.')
# else:
#     print('Classificação: Idoso')



# numero = int(input('Digite um valor: '))
# contador = 1
# maior = numero
# menor = numero

# while contador < 3: 
#     numero = int(input('Digite um valor: '))
#     contador += 1
#     if numero < menor:
#         menor = numero
#     if numero > maior:
#         maior = numero
# print(f'O maior número é {maior}')
# print(f'O menor número é {menor}')


# pares = 0
# impares = 0

# for i in range(10):

#     numero = int(input(f'Digite o {i +1} valor: '))
#     if i %2 == 0:
#         pares += 1
#     elif i %2 != 0:
#         impares += 1

# print(pares)
# print(impares)


# soma = 0
# quantidade_pessoas = int(input('Quantas pessoas você quer inserir?: '))
# for i in range(quantidade_pessoas):
#     idade = int(input(f'Digite a idade da {i +1} pessoa: '))
#     soma += idade
#     media = soma / quantidade_pessoas
# if media >= 0 and media <=25:
#         print(f'A média da turma foi: {media}\nA turma é jovem.')
# elif media <= 60:
#         print(f'A média da turma é: {media}\nA turma é adulta')
# elif media > 60: 
#         print(f'A média da turma é maior que 60.\nA turma é idosa.')



# conjunto = (10, 36, 2, 40, 25)
# print(f'O menor valor do do conjunto é: {min(conjunto)}')
# print(f'O maior valor do conjunto é: {max(conjunto)}')
# print(f'A soma dos valores do conjunto é: {sum(conjunto)}')


produtos = []
total_gasto = 0
quantidade_produtos_1000 = 0

nome_produto_mais_barato = None

while True:

    nome_produto = input('Digite o nome do produto: ')
    valor_produto = float(input('Digite o valor do produto: '))
    produtos.append(nome_produto)
    produtos.append(valor_produto)
    produto_mais_barato = valor_produto
    total_gasto += valor_produto

    if valor_produto > 1000:
        quantidade_produtos_1000 += 1
    if valor_produto < produto_mais_barato:
        nome_produto_mais_barato = nome_produto
    continuar = input('Deseja continuar? [S/N]: ').upper().strip()[0]
    if continuar == 'S':
        continue
    else:
        break
    
print(total_gasto)
print(quantidade_produtos_1000)
print(nome_produto_mais_barato)
