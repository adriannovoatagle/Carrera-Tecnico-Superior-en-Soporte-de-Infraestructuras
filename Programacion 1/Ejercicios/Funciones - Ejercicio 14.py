def inv():
    x = input('Ingrese texto: ')
    t = ''
    for i in (x[::-1]):
        t += i
    return t

print ('El texto invertido es:',inv())
