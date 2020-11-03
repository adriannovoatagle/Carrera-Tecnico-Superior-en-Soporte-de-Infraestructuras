def caracter():
    x = input('Ingrese caracter: ')
    vo = 'aeiou'
    for i in x:
        for z in vo:
            if i == z:
                return True
            else:
                return False
    
print (caracter())
