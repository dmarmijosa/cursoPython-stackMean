from ast import Num
import numpy


import numpy
import random
arreglo =[]
numeroImpar=0
for i in range(0,10):
    arreglo.append(random.randint(0,100))

for i in arreglo:
    if(i%2 != 0):
        numeroImpar=numeroImpar+i

print(f"En el arreglo: \n{arreglo} \nla suma de los numeros impares es: \n{numeroImpar}")
