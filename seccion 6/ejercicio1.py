class Vehiculo:
    color='rojo'
    ruedas='4'
    puerta='4'

class Coche(Vehiculo):
    velocidad=None
    cilindrada=None
    def __init__(self):
        self.velocidad='150km/h'
        self.cilindrada='1.5'
auto = Coche();
print(auto.color,' ',auto.ruedas,' ',auto.puerta,' ',auto.velocidad,' ',auto.cilindrada)