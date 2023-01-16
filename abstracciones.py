
class Lavadora:
    def __init__(self):
        pass
    def lavar(self, temperatura = input ('ingrese modo: ')): #aqui se define el argumento para temperatura
        self._llenar_tanque_agua(temperatura)
        self._jabon()
        self._lavar()
        self._centrifugar()
    
    def _llenar_tanque_agua(self, temperatura):
        print(f'llenando el tanque de agua en modo {temperatura}')
    def _jabon(self):
        print(f'agregando jabón')
    def _lavar(self):
        print(f'lavando')
    def _centrifugar(self):
        print(f'centrifugando')
# Hasta aquí tenemos la abstracción, el usuario no necesita todo esto para poder usar la lavadora

#Interfaz:
if __name__ == '__main__':
    lavadora = Lavadora()
    lavadora.lavar()


