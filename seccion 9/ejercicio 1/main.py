arreglo=[]

for i in range(0,5):
    arreglo.append(int(input(f'Ingrese el valor del {i+1}:\n')))


print(f"Estos son los datos originales: \n",arreglo)
print(f"Estos son los datos sin suplicados: \n{set(arreglo)}")