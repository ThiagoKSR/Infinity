from time import sleep

class Animal:
    def falar(self):
        print('Este animal faz um som')
        print('...')
        
class Cachorro(Animal):
    def falar(self):
        print('O cachorro faz AU AU')
        print('...')

class Gato(Animal):
    def falar(self):
        print('O gato faz MIAU')

animal = Animal()
cachorro = Cachorro()
gato = Gato()

animal.falar()
sleep(1.5)

cachorro.falar()
sleep(1.5)

gato.falar()
