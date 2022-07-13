from vehiculo import Vehiculo 
auto = Vehiculo(str(4),'rojo','ford','fx503')

f = open('./vehiculo.txt','w')
f.writelines("%s|" % l for l in [str(auto.color),auto.rueda,auto.marca,auto.modelo])
f.close()

f = open('./vehiculo.txt','r')
print(f.readlines())
f.close()