def ordenada():
    x = list((input(str('Ingrese datos: '))))
    r = x.copy()
    x.sort()
    if x == r:
        return True
    else:
        return False

print(ordenada())
    
    
    

