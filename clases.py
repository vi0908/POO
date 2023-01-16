#definición de la clase
class Persona:
    def __init__(self, nombre, edad):
     #variables de instancia
        self.nombre = nombre
        self.edad = edad
     #método de instancia
    def saluda(self, otra_persona):
        return f' Hola {otra_persona.nombre}, me llamo {self.nombre}'

#uso
david = Persona('David', 35)
erika = Persona('Erika', 30) 

print(david.saluda(erika))
print(david.edad)
