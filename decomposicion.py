
class Automovil:
    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'en reposo' #variable privada, notar el guión bajo
        self._motor = Motor(cilindros = 4) #clase dentro de clase

    def acelerar(self, tipo ='despacio'):
        self._estado = 'en movimiento'
    

class Motor:
    def __init__(self, cilindros, tipo = 'gasolina' ): #parámeto definido
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0
    def inyecta_gasolina(self, cantidad):
        pass

if __name__ == '__main__':
    carro_1 = Automovil('Nissan', 'Versa', 'Negro')
    carro_1.acelerar()
    print(carro_1._estado)
