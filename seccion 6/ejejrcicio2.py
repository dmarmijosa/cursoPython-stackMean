from ast import alias
from mimetypes import init


class Alumno:
    nombre:None
    nota:None
    def __init__(self, nombre,nota):
        self.nombre=nombre
        self.nota=nota
        
    def aprobado(self):
        if(self.nota >= 7 ):
            print('Aprobado')
        else:
            print('no aprobado')



alumno =  Alumno('Danny',7.5)
alumno.aprobado()