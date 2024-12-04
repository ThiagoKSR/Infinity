#Crie uma função chamada lancar_dados que utilizará o módulo random para simular o lançamento de dois dados. 
#Cada dado deve gerar um número aleatório entre 1 e 6. 
#A função deve somar os resultados desses dois lançamentos e retornar o valor total.

from random import randint

def lancar_dados(dado_1, dado_2):
    return dado_1 + dado_2

print('-'*20)
print('LANÇAR DADOS:')
print('-'*20)

dado_1 = randint(1, 6)
dado_2 = randint(1, 6)

resultado = lancar_dados(dado_1, dado_2)
print('-'*30)
print('RESULTADOS:')
print('-'*30)
print(f'O dado número 01 deu: {dado_1}')
print(f'O dado número 02 deu: {dado_2}')
print('-'*30)
print('TOTAL:')
print('-'*30)
print(f'A soma dos resultados é: {resultado}')