# class Carro:
#     def __init__(self, modelo, cor, ano):
#         self.modelo = modelo
#         self.cor = cor
#         self.ano = ano
#         self.velocidade = 0

# fusca = Carro("Fusca", "Verde", 1984)

# print(fusca)


# class Computador:
#     def __init__(self, cor, processador, monitor, teclado, mouse):
#         self.cor = cor
#         self.processador = processador
#         self.monitor = monitor
#         self.teclado = teclado
#         self.mouse = mouse
#     def __str__(self):
#         return f"Cor: {self.cor}\nProcessador: {self.processador}\nMonitor: {self.monitor}\nTeclado: {self.teclado}\nMouse{self.mouse}"

# maquina = Computador("Preto", "R5500", "Wide Screen 27pol", "Mecânico", "Logitec G7")

# print(maquina)


# class Calculadora:
#     def __init__(self, somar, subtrair, dividir, multiplicar):
#         self.somar = somar
#         self.subtrair = subtrair
#         self.dividir = dividir
#         self.multiplicar = multiplicar


#class Calculadora:
#     def __init__(self, somar, subtrair, dividir, multiplicar):
#         self.somar = somar
#         self.subtrair = subtrair
#         self.dividir = dividir
#         self.multiplicar = multiplicar

class Calculadora:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
    
    def somar(self):
        resultado = self.n1 + self.n2
        print(f"{self.n1} + {self.n2} = {resultado}")

    def subtrair(self):
        resultado = self.n1 - self.n2
        print(f"{self.n1} - {self.n2} = {resultado}")

    def multiplicar(self):
        resultado = self.n1 * self.n2
        print(f"{self.n1} * {self.n2} = {resultado}")

    def dividir(self):
        resultado = self.n1 / self.n2
        if n1 == 0:
            print('Divisão impossível')
        else:
            print(f"{self.n1} / {self.n2} = {resultado}")

    
n1 = int(input('Insira um número: '))
n2 = int(input('Insira outro número: '))
resultado = Calculadora(n1, n2)
resultado.somar()
resultado.subtrair()
resultado.dividir()
resultado.dividir()


