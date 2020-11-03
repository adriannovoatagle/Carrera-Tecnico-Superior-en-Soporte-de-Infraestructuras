cm = str(input('Ingrese clave maestra: '))
c1 = ''
c2 = ''
for i in cm:
    if int(i) % 2 != 0:
        c1 += i
    else:
        c2 += i
        
print ('Clave 1: ',c1)
print ('Clave 2: ',c2)
