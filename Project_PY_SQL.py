import mysql.connector

class BancoDeDados:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="Aluno123",
            database="estoque"
        )
        self.cursor = self.conexao.cursor()
        print("Conexão com o banco foi estabelecida com sucesso!")
        self.criar_tabelas()
    
    def criar_tabelas(self):
        comando_criar_produtos = """
            CREATE TABLE IF NOT EXISTS produtos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                descricao TEXT,
                quantidade INT NOT NULL,
                preco DECIMAL(10, 2) NOT NULL
            )
        """
        self.cursor.execute(comando_criar_produtos)

        comando_criar_vendas = """
            CREATE TABLE IF NOT EXISTS vendas (
                id INT AUTO_INCREMENT PRIMARY KEY,
                produto_id INT,
                quantidade INT NOT NULL,
                data_venda DATETIME NOT NULL,
                FOREIGN KEY (produto_id) REFERENCES produtos(id)
            )
        """
        self.cursor.execute(comando_criar_vendas)
        self.conexao.commit()
        print("Tabelas criadas/verificadas com sucesso!")

class Sistema:
    def __init__(self):
        self.bd = BancoDeDados()
        

    def adicionar_produto(self, novo_produto):
        if not novo_produto.nome or novo_produto.qtde < 0 or novo_produto.preco <= 0:
            print("Dados do produto inválidos")
            return None
        
        comando = """
            INSERT INTO produtos (nome, descricao, quantidade, preco)
            VALUES (%s, %s, %s, %s)
        """
        dados = (novo_produto.nome, novo_produto.descricao, novo_produto.qtde, novo_produto.preco)
        self.bd.cursor.execute(comando, dados)
        self.bd.conexao.commit()
        novo_id = self.bd.cursor.lastrowid
        print(f"Produto {novo_produto.nome} adicionado com sucesso!")
        return novo_id

    def listar_produtos(self):
        self.bd.cursor.execute("SELECT * FROM produtos")
        produtos = []
        for produto in self.bd.cursor.fetchall():
            produtos.append(
                Produto(
                    id=produto[0],
                    nome=produto[1],
                    descricao=produto[2],
                    qtde=produto[3],
                    preco=produto[4]
                )
            )
        if not produtos:
            print("Nenhum produto cadastrado!")
        
        return produtos

    def editar_produto(self):
        pass

class Produto:
    def __init__(self, nome, descricao, qtde, preco, id=None):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.qtde = qtde
        self.preco = preco

class Venda:
    def __init__(self, id, produto_id, qtde, data_venda):
        self.id = id
        self.produto_id = produto_id
        self.qtde = qtde
        self.data_venda = data_venda

sistema = Sistema()
while True:
    print("------------ESTOQUE v0.1-------------")
    print("1 - Adicionar novo produto")
    print("2 - Listar produtos")
    print("3 - Sair")
    op = int(input("-> "))
    if op == 1:
        nome = input("Digite o nome do produto: ")
        descricao = input("Digite a descrição do produto: ")
        qtde = int(input("Digite a quantidade do produto: "))
        preco = float(input("Digite o preço do produto: "))
        novo_produto = Produto(nome, descricao, qtde, preco)
        sistema.adicionar_produto(novo_produto)
    elif op == 2:
        produtos = sistema.listar_produtos()
        print("---------PRODUTOS CADASTRADOS----------")
        for produto in produtos:
            print(f"ID: {produto.id}")
            print(f"Nome: {produto.nome}")
            print(f"Quantidade em estoque: {produto.qtde}")
            print(f"Preço Unitário: {produto.preco}")
            print(f"Descrição: {produto.descricao}")
            print("----------------------\n")
    elif op == 3:
        print("Desligando o sistema...")
        break
        