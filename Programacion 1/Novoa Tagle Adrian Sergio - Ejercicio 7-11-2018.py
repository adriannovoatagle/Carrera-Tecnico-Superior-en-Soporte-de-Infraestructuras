# Nombre y Apellido: Adrian Sergio Novoa Tagle.
#
# Ejercicio:
# Hacer un programa que tenga las siguientes funciones

# * decabin > convierte un número decimal entero a binario
# * binadec > convierte un número binario a decimal
# * binahex > convierte un número binario a hexadecimal

# Dada una ip el programa debe convertir la direccion a binario y a hexadecimal.

# Dado un número binario (ej.: 00100101) convertirlo a decimal

# Permitir al usuario una vez cargado el programa ejecutar las funciones
# tantas veces como desee el usuario sin salir del programa.

import os

def menu():
    
    os.system('cls')    
    opciones = str(input('\nMenu - Elija una opcion:\n' + '\n' +
                         '1 - decabin > convierte un número decimal entero a binario\n' + 
                         '2 - binadec > convierte un número binario a decimal\n' + 
                         '3 - binahex > convierte un número binario a hexadecimal\n' +
                         '4 - Dada una ip el programa debe convertir la direccion a binario y a hexadecimal\n' + 
                         '5 - Dado un número binario (ej.: 00100101) convertirlo a decimal\n' +
                         '6 - Salir\n\n' + 
                         'Opcion: ')) 
    if opciones == '1':
        os.system('cls')
        print('decabin > convierte un número decimal entero a binario:\n')
        decabin()
    elif opciones == '2':
        os.system('cls')
        print('binadec > convierte un número binario a decimal:\n')
        binadec()
    elif opciones == '3':
        os.system('cls')
        print('binahex > convierte un número binario a hexadecimal:\n') 
        binahex()
    elif opciones == '4':
        os.system('cls')
        print('Dada una ip el programa debe convertir la direccion a binario y a hexadecimal:\n')
        ipbinhex()
    elif opciones == '5':
        os.system('cls')
        print('Dado un número binario (ej.: 00100101) convertirlo a decimal\n')
        numbindec()
    elif opciones == '6':
        exit()
    else:
        input('\nSeleccion incorrecta. Presione "Enter" para elejir nuevamente.')
        os.system('cls')
        menu()


def decabin():

    x = int(input('\nIngrese un numero: '))
    y = bin(x)
    print('\nEl numero ingresado en binario es igual a: ' + y.replace('0b',''))
   
    terminado = input('\n\nOpciones:\n\n' +
                      '1 - Ingresar otro numero\n' +
                      '2 - Menú Principal\n' +
                      '3 - Salir\n\n' +
                      'Opcion: ')
    if terminado == '1':
        os.system('cls')
        decabin()
    elif terminado == '2':
        os.system('cls')
        menu() 
    elif terminado == '3':
        exit()

        
def binadec():
  
    x = input('\nIngrese un numero en binario: ')
    print('\nEl numero ingresado en decimal es igual a: ', int(x,2))

    terminado = input('\n\nOpciones:\n\n' +
                      '1 - Ingresar otro numero\n' +
                      '2 - Menú Principal\n' +
                      '3 - Salir\n\n' +
                      'Opcion: ')
    if terminado == '1':
        os.system('cls')
        binadec()
    elif terminado == '2':
        os.system('cls')
        menu() 
    elif terminado == '3':
        exit()


def binahex():

    x = input('\nIngrese un numero en binario: ')
    xbin = int(x,2)
    xhex = hex(xbin)
    
    print('\nEl numero ingresado en hexadecimal es igual a: ' + xhex.replace('0x','').upper())
   
    terminado = input('\n\nOpciones:\n\n' +
                      '1 - Ingresar otro numero\n' +
                      '2 - Menú Principal\n' +
                      '3 - Salir\n\n' +
                      'Opcion: ')
    if terminado == '1':
        os.system('cls')
        binahex()
    elif terminado == '2':
        os.system('cls')
        menu() 
    elif terminado == '3':
        exit()


def ipbinhex():

    
    dirip = input('\nIngrese direccion ip: ')
    diripsp = dirip.split('.')

    #Conversion a binario
    dirip0 = str(bin(int(diripsp[0])).replace('0b',''))
    dirip1 = str(bin(int(diripsp[1])).replace('0b',''))
    dirip2 = str(bin(int(diripsp[2])).replace('0b',''))
    dirip3 = str(bin(int(diripsp[3])).replace('0b',''))

    if dirip0 == '0':
        dirip0 = '00000000'
    if dirip1 == '0':
        dirip1 = '00000000'
    if dirip2 == '0':
        dirip2 = '00000000'
    if dirip3 == '0':
        dirip3 = '00000000'
        
    #Si por ejemplo el valor obtenido en la conversión es '10' se convierte al formato '00000010'.    
    diripbin0 = 8 - len(dirip0)
    diripbin1 = 8 - len(dirip1)
    diripbin2 = 8 - len(dirip2)
    diripbin3 = 8 - len(dirip3)
    diripreal0 = ''
    diripreal1 = ''
    diripreal2 = ''
    diripreal3 = ''

    for di in range(0,diripbin0): #Valor obtenido en 1er octeto de la direccion se convierte al formato 'xxxxxxxx'.
        diripreal0 += '0'
    diripreal0 += dirip0
    for di in range(0,diripbin1):
        diripreal1 += '0'
    diripreal1 += dirip1
    for di in range(0,diripbin2):
        diripreal2 += '0'
    diripreal2 += dirip2
    for di in range(0,diripbin3):
        diripreal3 += '0'
    diripreal3 += dirip3

    diripbinfinal = diripreal0 + '.' + diripreal1 + '.' + diripreal2 + '.' + diripreal3
    
    #Conversion a hexadecimal
    diriphex0 = str(hex(int(diripsp[0])).replace('0x',''))
    diriphex1 = str(hex(int(diripsp[1])).replace('0x',''))
    diriphex2 = str(hex(int(diripsp[2])).replace('0x',''))
    diriphex3 = str(hex(int(diripsp[3])).replace('0x',''))

    if diriphex0 == '0':
        diriphex0 = '00'
    if diriphex1 == '0':
        diriphex1 = '00'
    if diriphex2 == '0':
        diriphex2 = '00'
    if diriphex3 == '0':
        diriphex3 = '00'

    #Si por ejemplo el valor obtenido en la conversión es 'A' se convierte al formato '0A'.

    diriphexa0 = 2 - len(diriphex0)
    diriphexa1 = 2 - len(diriphex1)
    diriphexa2 = 2 - len(diriphex2)
    diriphexa3 = 2 - len(diriphex3)
    diriprealhex0 = ''
    diriprealhex1 = ''
    diriprealhex2 = ''
    diriprealhex3 = ''
    

    for dih in range(0,diriphexa0): #Valor obtenido en 1er octeto de la direccion se convierte al formato 'xx'.
        diriprealhex0 += '0'
    diriprealhex0 += diriphex0
    for dih in range(0,diriphexa1): 
        diriprealhex1 += '0'
    diriprealhex1 += diriphex1
    for dih in range(0,diriphexa2): 
        diriprealhex2 += '0'
    diriprealhex2 += diriphex2
    for dih in range(0,diriphexa3): 
        diriprealhex3 += '0'
    diriprealhex3 += diriphex3
        
    diriphexfinal = diriprealhex0 + '.' + diriprealhex1 + '.' + diriprealhex2 + '.' + diriprealhex3
    
    print('\nLa dirección ip convertida en binario es igual a: ' + diripbinfinal)
    print('La dirección ip convertida en hexadecimal es igual a: ' + diriphexfinal.upper())


    terminado = input('\n\nOpciones:\n\n' +
                      '1 - Ingresar otra dirección ip\n' +
                      '2 - Menú Principal\n' +
                      '3 - Salir\n\n' +
                      'Opcion: ')
    if terminado == '1':
        os.system('cls')
        ipbinhex()
    elif terminado == '2':
        os.system('cls')
        menu() 
    elif terminado == '3':
        exit()


def numbindec():

    binadec()
    

menu()
