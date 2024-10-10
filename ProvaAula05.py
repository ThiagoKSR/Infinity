# Desenvolva um programa em Python para calcular a média de notas de alunos em uma disciplina. 
# O programa deve solicitar ao usuário o número de alunos e, em seguida, para cada aluno, pedir o nome e três notas. 
# Utilize um loop 'for' para iterar sobre os alunos e suas notas.
# Além disso, implemente uma estrutura condicional para verificar se cada aluno foi aprovado ou reprovado, considerando que a média mínima para aprovação é 7.0. 
# Exiba o nome do aluno, suas notas, média e a indicação de aprovação ou reprovação.
# Ao final, exiba a média geral da turma.

total_notas = 0
alunos = int(input('Digite o número de alunos: '))
print('+='*40)
quantidade_alunos = alunos
for i in range(alunos):

    nome = input(f'Digite o nome do {i+1}º aluno: ')
    nota_1 = float(input('Digite o valor da primera nota: '))
    nota_2 = float(input('Digite o valor da segunda nota: '))
    nota_3 = float(input('Digite o valor da terceira nota: '))
    media = (nota_1 + nota_2 + nota_3) / 3
    print(f'As notas do aluno {nome} foram: {nota_1}, {nota_2}, {nota_3}')
    print(f'A média do aluno {nome} foi: {media:.2f}')
    
    total_notas += nota_1 + nota_2 + nota_3

    if media >= 7:
        print(f'O aluno {nome} foi aprovado!')
        print('+='*40)
    else:
        print(f'O aluno {nome} foi reprovado.')
        print('+='*40)

print(f'A média geral da turma foi: {total_notas / (alunos * 3):.2f}')
print('+='*40)