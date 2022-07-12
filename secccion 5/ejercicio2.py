def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            print("No es primo")
            return False
    print("Es primo")
    return True

v = int(input('ingrese el año a verificar '))

es_primo(v)
