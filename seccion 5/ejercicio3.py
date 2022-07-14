def es_bisiesto(num):
    if (num % 4==0) or (num %100 ==0 ) and (num%400==0):
        print('Es bisiesto')
    else:
        print('no es bisisesto')

v = int(input('ingrese el año a verificar '))

es_bisiesto(v)
