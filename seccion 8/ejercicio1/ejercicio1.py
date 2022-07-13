

f = open("./archivo.txt","w")
f.writelines(['Bienvenidos a python\n','Lenguaje de programación alto nivel'])
f.close()



f = open("./archivo.txt","r")


print(f.readlines())
f.close()
