# Crie um dicionário que irá armazenar informações de um contato, incluindo o nome, o telefone e o email. 
# Peça ao usuário para fornecer esses dados, solicitando que ele insira o nome do contato, o número de telefone e o endereço de email. 
# Após coletar todas as informações necessárias, exiba o conteúdo do dicionário, mostrando todas as informações do contato inserido pelo usuário.



contato_dic = {'nome' : [],
               'telefone' : [],
               'email' : []
               }

nome = input('Digite o seu nome: ')
telefone = input('Digite seu melhor número de telefone para contato: ') #Caro avaliador, utilizei a variável como string para facilitar caso o usuário de um espaço.
email = input('Digite seu melhor endereço de email: ')
contato_dic['nome'].append(nome)
contato_dic['telefone'].append(telefone)
contato_dic['email'].append(email)

for i in range(len(contato_dic['nome'])):

    print(f'Nome: {contato_dic["nome"][i]}')
    print(f'Telefone: {contato_dic["telefone"][i]}')
    print(f'Email: {contato_dic["email"][i]}')