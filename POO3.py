class ContaBancaria:
    def __init__(self, titular):
        self.__saldo = 3000
        self.__titular = titular

    def get_saldo(self):
        return self.__saldo
    
    def get_titular(self):
        return self.__titular

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"R${valor} foi depositado a sua conta!")
        else:
            print("Valor de depósito inválido")

    def sacar(self, valor):
        if self.__saldo > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
                print(f"R${valor} foi retirado de sua conta!")
            else:
                    print("Saldo insuficiente!")
        else:
            print("Valor de saque inválido!")
    

    def exibir_saldo(self):
        print(f"Seu saldo é: R${self.__saldo}")
        return
    
conta = ContaBancaria("Thiago")
conta.depositar(100)
conta.sacar(400)
conta.exibir_saldo()
