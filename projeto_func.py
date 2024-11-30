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
    for tarefa in banco_de_dados:
        print(f'Nome: {tarefa["nome"]}')
        print(f'Descrição: {tarefa["descrição"]}') 
        print(f'Data: {tarefa["data"]}')
        print(f'Concluido:{tarefa["concluido"]}')
        print()

def prioridade_tarefa():
    escolha = int(input('Escolha a prioridade da tarefa: '))
    for tarefa in banco_de_dados:
        if tarefa['prioridade'] == escolha:
            print(f'Nome: {tarefa["nome"]}')
            print(f'Descrição: {tarefa["descrição"]}')
            print(f'Prioridade: {tarefa["prioridade"]}')
            print(f'Categoria: {tarefa["categoria"]}')
            print(f'Data: {tarefa["data"]}')
            print(f'Concluido:{tarefa["concluido"]}')
            print('-'*40)  
                                        
def categoria_tarefa():
    escolha = input('Digite o nome da categoria: ')
    for item in banco_de_dados:
        if item['categoria'].lower() == escolha:
            print(f'Nome: {item["nome"]}')
            print(f'Descrição: {item["descrição"]}')
            print(f'Prioridade: {item["prioridade"]}')
            print(f'Categoria: {item["categoria"]}')
            print(f'Data: {item["data"]}')
            print(f'Concluido:{item["concluido"]}')
            print('-'*40)
        
def editar_tarefa():
    nome = input('Digite o nome da tarefa a ser editada: ')
    for tarefa in banco_de_dados:
            if tarefa['nome'] == nome:
                print('Campos disponiveis para edição: Nome, Descrição, Prioridade, Categoria, Data, Concluido.')
                campo = input('Digite o nome do campo a ser editado: ').lower()
                if campo in tarefa:
                    if campo == 'nome':
                        tarefa[campo] = input('Digite um novo valor para o campo: ')
                    elif campo == 'descrição':
                        tarefa[campo] = input('Digite um novo valor para o campo: ')
                    elif campo == 'prioridade':
                        tarefa[campo] = int(input('Digite um novo valor para o campo: '))
                    elif campo == 'categoria':
                        tarefa[campo] = input('Digite um novo valor para o campo: ')
                    elif campo == 'data':
                        tarefa[campo] = input('Digite um novo valor para o campo: ')
                    elif campo == 'Concluido':
                        nova_conclusao = input('Digite "sim" ou "não" para marcar: ')
                        tarefa[campo] = (nova_conclusao == 'sim')
                    print('Tarefa editada com sucesso.')
                    return
                else:
                    print('Campo inválido.\n')
                    return
    print('Tarefa não encontrada.\n')
                    
def conclui_tarefa():
    nome = input('Informe o nome da tarefa a ser concluída: ')
    for tarefa in banco_de_dados:
            if tarefa['nome'] == nome:
                tarefa['concluido'] = True
                print('Tarefa marcada como concluída.\n')
                return
    print('Tarefa não encontrada.')

def deletar_tarefa():
    nome = input('Insira o nome da tarefa a ser deletada: ')
    for tarefa in banco_de_dados:
            if tarefa['nome'] == nome:
                banco_de_dados.remove(tarefa)
                print('Tarefa removida com sucesso.\n')
                return
    print('Tarefa não encontrada.\n')                


    
    

while True:
    print(
        '1 - Adicionar tarefa\n'
        '2 - Listar tarefas\n'
        '3 - Prioridade\n'
        '4 - Categorias\n'
        '5 - Editar tarefas\n'
        '6 - Concluir\n'
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
    if escolha == 6:
        conclui_tarefa()
    if escolha == 7:
        deletar_tarefa()
    if escolha == 8:
        break
print('Programa encerrado.')
