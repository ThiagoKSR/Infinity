#Importe o módulo 'os' e use a função 'listdir' para listar todos
#os arquivos e pastas presentes no diretório onde o script Python está sendo executado. 
#A função 'listdir' retornará uma contendo os nomes dos arquivos e pastas. 
#Após obter essa lista, exiba cada item da lista individualmente na saída do console.

from os import listdir


diretorio = 'D:\AULA01\Curso em vídeo'

conteudo = listdir(diretorio)

for arquivo in conteudo:
    print(f'{arquivo}')
