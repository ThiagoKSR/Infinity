#Crie uma função chamada media que receberá três números como argumentos. 
#Esta função deve calcular a média aritmética desses três números. 
#Para fazer isso, some os três números e, em seguida, divida o resultado por três. 
#Por fim, a função deve retornar o valor da média aritmética calculada.

def media():
    total = 0
    for n in range(3):
        nota = float(input(f'Digite a {n +1}º nota do aluno: '))
        total += nota
    media = total / 3
    return media
resultado = media()

print(f'A média do aluno é: {resultado:.2f}')
