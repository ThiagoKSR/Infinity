# [LPIA-A03] Você está criando um programa em Python para simular um jogo simples de adivinhação. 
# O programa deve ter um número fixo, por exemplo, 7, que o jogador deve adivinhar. 
# O jogador terá até 3 tentativas para acertar o número.
# Implemente o jogo utilizando um loop while para permitir que o jogador faça múltiplas tentativas até acertar ou atingir o limite de tentativas. 
# Utilize a estrutura else para exibir uma mensagem de encorajamento caso o jogador acerte e uma mensagem de consolo caso as 3 tentativas se esgotem sem sucesso.

numero_fixo = 7
numero_tentativas = 3
contador = 1
print('Tente advinhar em qual número estou pensando!!!')
escolha = int(input('Digite um número entre 0 e 10: '))
while escolha != numero_fixo:
    escolha = int(input('Digite um número entre 0 e 10: '))
    contador += 1
    if escolha == numero_fixo:
        print('Parabéns. Você acertou!')
        print(f'Você utilizou {contador} tentativas.')
        break
    else:
        if contador == numero_tentativas:
            print('Não foi dessa vez.\nTente novamente.')
            break
