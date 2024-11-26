banco_de_dados = []

def adicionar_tarefa():
    tarefa = {
        'nome': input('Digite o nome da tarefa: '),
        'descrição': input('Digite a descrição da tarefa: '),
        'prioridade': int(input('Digite a prioridade (1-5): ')),
        'categoria': input('Digite a categoria da tarefa: '),
        'data': input('Digite a data: '),
        'concluido': False
    }

    banco_de_dados.append(tarefa)
    print('Tarefa adicionada com sucesso.')
    print()


def listar_tarefas():
    for item in banco_de_dados:
        print(f'Nome: {item['nome']}')
        print(f'Descrição: {item['descrição']}')
        
        
        print(f'Data: {item['data']}')
        print(f'Concluido:{item['concluido']}')
        print()


def prioridade_tarefa():
    escolha = int(input('Escolha a prioridade da tarefa: '))
    for item in banco_de_dados:
        if item['prioridade'] == escolha:
            print(f'Nome: {item['nome']}')
            print(f'Descrição: {item['descrição']}')
            print(f'Prioridade: {item['prioridade']}')
            print(f'Categoria: {item['categoria']}')
            print(f'Data: {item['data']}')
            print(f'Concluido:{item['concluido']}')
            print('-'*40)  
                                        

def categoria_tarefa():
    escolha = input('Digite o nome da categoria: ')
    for item in banco_de_dados:
        if item['Categoria'] == escolha:
            print(f'Nome: {item['nome']}')
            print(f'Descrição: {item['descrição']}')
            print(f'Prioridade: {item['prioridade']}')
            print(f'Categoria: {item['categoria']}')
            print(f'Data: {item['data']}')
            print(f'Concluido:{item['concluido']}')
            print('-'*40)
        
def editar_tarefa():
    escolha = input('Digite o nome da tarefa a ser editada: ')
    if escolha in banco_de_dados:
        escolha_campo = input('Digite o nome do campo a ser editado: ')
        if escolha_campo in banco_de_dados[escolha]:
            banco_de_dados[escolha_campo] = input('Digite o novo status ou nome: ')
            print('Tarefa editada')

    

while True:
    print(
        '1 - Adicionar tarefa\n'
        '2 - Listar tarefas\n'
        '3 - Prioridade\n'
        '4 - Categorias\n'
        '5 - Editar tarefas\n'
        '6 - Marcar conclusão\n'
        '7 - Deletar\n'
        '8 - Sair\n'
        )

    escolha = int(input('Digite a opção desejada: '))
    if escolha == 1:
        adicionar_tarefa()
    if escolha == 2:
        listar_tarefas()
    if escolha == 3:
        prioridade_tarefa()
    if escolha == 4:
        categoria_tarefa()
    if escolha == 5:
        editar_tarefa()

        
