#Crie um dicionário para armazenar o nome e o preço de cinco produtos. 
#Peça ao usuário para inserir o nome de cada produto e o respectivo preço. 
#À medida que o usuário fornece os dados, armazene cada produto como uma chave no dicionário e o preço como o valor associado a essa chave. 
#Após a inserção de todos os produtos e preços, calcule o valor total da compra somando todos os preços armazenados no dicionário. 
#Por fim, exiba o valor total da compra.



produto_valor = {}

for produto in range(5):
    nome = input('Digite o nome do produto: ').capitalize()
    valor = float(input('Digite o valor do produto: '))
    produto_valor[nome] = valor
print()

for item, preco in produto_valor.items():
    print(f'Nome do produto: {item}')
    print(f'Valor do produto: R${preco:.2f}')
    print('-'*20)