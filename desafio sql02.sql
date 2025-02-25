create database loja_online;

use loja_online;

create table produtos(
id varchar(255),
nome varchar(255),
preco int,
estoque int)
;

insert into produtos(id, nome, preco, estoque) values
('P001', 'Cadeira de Escritório', 199, 50),
('P002', 'Mesa de Jantar', 450, 30),
('P003', 'Sofá 3 Lugares', 899, 15),
('P004', 'Cama Queen Size', 1200, 20),
('P005', 'Micro-ondas 20L', 350, 40),
('P006', 'Geladeira 400L', 2200, 10),
('P007', 'Fogão 4 Bocas', 800, 25),
('P008', 'Televisor LED 50"', 1800, 12),
('P009', 'Notebook Intel i5', 3500, 8),
('P010', 'Smartphone 128GB', 2500, 60),
('P011', 'Ferro de Passar', 120, 100),
('P012', 'Luminária de Mesa', 75, 200),
('P013', 'Cama Box Solteiro', 350, 50),
('P014', 'Armário 3 Portas', 550, 45),
('P015', 'Ventilador de Teto', 160, 70),
('P016', 'Aspirador de Pó', 250, 35),
('P017', 'Roupão de Banho', 90, 150),
('P018', 'Jogo de Panelas', 250, 60),
('P019', 'Escova Elétrica', 150, 120),
('P020', 'Cafeteira Elétrica', 180, 90)
;

create table clientes(
id int,
nome varchar(255),
email varchar(255),
historico varchar(255))
;



insert into clientes(id, nome, email, historico) values
(1, 'João Silva', 'joao.silva@email.com', 'Cadeira de Escritório, Geladeira 400L, Sofá 3 Lugares'),
(2, 'Maria Oliveira', 'maria.oliveira@email.com', 'Mesa de Jantar, Ferro de Passar, Luminária de Mesa'),
(3, 'Carlos Pereira', 'carlos.pereira@email.com', 'Televisor LED 50", Fogão 4 Bocas, Cama Box Solteiro'),
(4, 'Ana Souza', 'ana.souza@email.com', 'Cama Queen Size, Sofá 3 Lugares, Ventilador de Teto'),
(5, 'Lucas Costa', 'lucas.costa@email.com', 'Micro-ondas 20L, Ferro de Passar, Jogo de Panelas'),
(6, 'Beatriz Lima', 'beatriz.lima@email.com', 'Cadeira de Escritório, Luminária de Mesa, Cama Box Solteiro'),
(7, 'Rafael Santos', 'rafael.santos@email.com', 'Notebook Intel i5, Ventilador de Teto, Escova Elétrica'),
(8, 'Fernanda Almeida', 'fernanda.almeida@email.com', 'Televisor LED 50", Luminária de Mesa, Cafeteira Elétrica'),
(9, 'Guilherme Pereira', 'guilherme.pereira@email.com', 'Geladeira 400L, Notebook Intel i5, Ventilador de Teto'),
(10, 'Mariana Santos', 'mariana.santos@email.com', 'Cama Box Solteiro, Jogo de Panelas, Ferro de Passar'),
(11, 'Pedro Martins', 'pedro.martins@email.com', 'Cama Queen Size, Armário 3 Portas, Luminária de Mesa'),
(12, 'Julia Rocha', 'julia.rocha@email.com', 'Ventilador de Teto, Ferro de Passar, Jogo de Panelas'),
(13, 'Ricardo Oliveira', 'ricardo.oliveira@email.com', 'Aspirador de Pó, Sofá 3 Lugares, Televisor LED 50"'),
(14, 'Larissa Ferreira', 'larissa.ferreira@email.com', 'Micro-ondas 20L, Cama Box Solteiro, Ventilador de Teto'),
(15, 'Gustavo Lima', 'gustavo.lima@email.com', 'Cadeira de Escritório, Cafeteira Elétrica, Jogo de Panelas'),
(16, 'Camila Souza', 'camila.souza@email.com', 'Cama Box Solteiro, Ferro de Passar, Ventilador de Teto'),
(17, 'Thiago Silva', 'thiago.silva@email.com', 'Roupão de Banho, Televisor LED 50", Fogão 4 Bocas'),
(18, 'Raquel Pereira', 'raquel.pereira@email.com', 'Luminária de Mesa, Cama Box Solteiro, Cafeteira Elétrica'),
(19, 'Felipe Costa', 'felipe.costa@email.com', 'Notebook Intel i5, Luminária de Mesa, Escova Elétrica'),
(20, 'Sabrina Almeida', 'sabrina.almeida@email.com', 'Cadeira de Escritório, Geladeira 400L, Jogo de Panelas')
;

create table pedidos(
id int, 
data_pedido varchar(255), 
id_cliente int, 
status_pedido varchar(255))
; 

insert into pedidos(id, data_pedido, id_cliente, status_pedido) values
(1, '2025-02-01', 1, 'Enviado'),
(2, '2025-02-02', 2, 'Cancelado'),
(3, '2025-02-03', 3, 'Em Processamento'),
(4, '2025-02-04', 4, 'Enviado'),
(5, '2025-02-05', 5, 'Entregue'),
(6, '2025-02-06', 6, 'Em Processamento'),
(7, '2025-02-07', 7, 'Enviado'),
(8, '2025-02-08', 8, 'Entregue'),
(9, '2025-02-09', 9, 'Cancelado'),
(10, '2025-02-10', 10, 'Enviado'),
(11, '2025-02-11', 11, 'Em Processamento'),
(12, '2025-02-12', 12, 'Entregue'),
(13, '2025-02-13', 13, 'Enviado'),
(14, '2025-02-14', 14, 'Cancelado'),
(15, '2025-02-15', 15, 'Em Processamento'),
(16, '2025-02-16', 16, 'Enviado'),
(17, '2025-02-17', 17, 'Entregue'),
(18, '2025-02-18', 18, 'Em Processamento'),
(19, '2025-02-19', 19, 'Cancelado'),
(20, '2025-02-20', 20, 'Enviado')
;

create table itens_pedido(
id int,
id_pedido int,
id_produto int,
quantidade_produto int)
;

insert into itens_pedido (id, id_pedido, id_produto, quantidade_produto) values
(1, 1, 1, 2),
(2, 1, 6, 1),
(3, 2, 3, 1),
(4, 3, 4, 2),
(5, 3, 9, 1),
(6, 4, 5, 1),
(7, 4, 7, 1),
(8, 5, 10, 1),
(9, 5, 3, 1),
(10, 6, 2, 1),
(11, 6, 14, 1),
(12, 7, 8, 1),
(13, 7, 15, 2),
(14, 8, 18, 3),
(15, 9, 17, 1),
(16, 10, 16, 1),
(17, 10, 12, 1),
(18, 11, 1, 1),
(19, 12, 19, 2),
(20, 13, 20, 1);











