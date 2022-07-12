import math

from numpy import double


def areaTriangulo(base:double,altura:double):
    return (base*altura)/2

def areaCirculo(radio:double):
    return math.pi*math.pow(radio,2);

base = double(input('ingrese la base del triagulo: '))
altura  = double(input('ingrese la altura del triagulo: '))

print('El area del triangulo es: ',areaTriangulo(base,altura))
radio = double(input('Ingrese el area del circulo: '))
print('El area del circulo es: ', areaCirculo(radio))