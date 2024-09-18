# Você está criando um programa para calcular a área de um retângulo. 
# O programa deve solicitar ao usuário que forneça a base e a altura do retângulo. 
# Em seguida, o programa deve calcular a área usando a fórmula:
# Área=Base×Altura

print('Olá, vou te ajudar a calcular a área de um retângulo! Vamos la?')
base = float(input('Qual o valor da base em Metros?: '))
altura = float(input('Qual o valor da altura em Metros?:  '))
area = base * altura
print(f'A área desse retângulo é de: {area:.2f} Metros^2.')