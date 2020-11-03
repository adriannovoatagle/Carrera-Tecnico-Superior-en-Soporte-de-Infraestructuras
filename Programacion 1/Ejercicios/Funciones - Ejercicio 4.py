def n():
    x = int(input('Escriba un numero: '))
    y = int(input('Escriba otro numero: '))
    z = x % y
    return ('El resto entre el 1ero y 2do es: ' + str(z))
    
print(n())
