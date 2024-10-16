# # Crie um programa em Python que simule um sistema de login. 
# # O programa deve permitir ao usuário três tentativas para acertar o nome de usuário e a senha corretos. 
# # Caso o usuário erre as credenciais, o programa deve fornecer uma mensagem informando quantas tentativas restam. 
# # Se o usuário acertar, uma mensagem de boas-vindas deve ser exibida, e o programa deve terminar imediatamente.
# # Se todas as três tentativas falharem, o programa deve usar um loop for para exibir uma mensagem de "Acesso bloqueado" repetida três vezes.


login = 'thiago_klauber'
senha = 'admin@123'
max_tentativas = 3
mensagem_tentativas = 2  
contador = 1  

usuario = input('login: ')
usuario_senha = input('Password: ')


if usuario == login and usuario_senha == senha:
    print('Boas vindas ao portal IN School Recife.\nSeu acesso foi liberado')
    
else:
    while contador < max_tentativas:
        print('''
        Credenciais inválidas!!
        ''')
        print(f'Você tem {mensagem_tentativas} tentativas restantes.')
        
        usuario = input('login: ')
        usuario_senha = input('Password: ')
        
        mensagem_tentativas -= 1  
        contador += 1  

    if contador == max_tentativas and (usuario != login or usuario_senha != senha):
        for i in range(3):
            print('Acesso bloqueado.')
        print('FIM')