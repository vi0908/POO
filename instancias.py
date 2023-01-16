class Coordenada:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distancia(self, otra_coordenada):
       return((otra_coordenada.x - self.x)**2 + (otra_coordenada.y - self.y)**2)**0.5
 
if __name__ == '__main__':
    coord_1 = Coordenada(3,20)
    coord_2 = Coordenada(4, 50)
    coord_3 = Coordenada(int(input(f'ingrese un número: ')), int(input(f'ingrese otro número: ')))
    print (coord_1.distancia(coord_3))
    

        