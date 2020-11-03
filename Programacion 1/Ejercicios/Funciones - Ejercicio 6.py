def n():
    x = int(input('Ingrese precio: '))
    i = x * 1.21
    return ('El precio con IVA incluido es: ' + str(i))
    
print(n())
