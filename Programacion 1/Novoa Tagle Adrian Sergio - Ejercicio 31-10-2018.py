# Nombre y Apellido: Adrian Sergio Novoa Tagle.
#
# Información consultada para desarrollar el punto 1 del ejercicio:
#
# https://docs.microsoft.com/en-us/windows/desktop/wmisdk/wmi-start-page
# https://pypi.org/project/WMI/
# http://mobilesecurity.com.pa/que-es-wmi/
#
#
# ********************Importante********************
#
# Se debe instalar el paquete pywin32 ademas del archivo "WMI-1.4.9.win32", el cual puede descargarse desde:
# https://pypi.org/project/WMI/

import os
import wmi
import platform
import socket


def menu():
    
    os.system('cls')    
    opciones = str(input('\nMenu - Elija una opcion:\n' + '\n' +
                         '1 - Info HW Local\n' + 
                         '2 - Info ultima vez accedido de ...exe (elija el exe)\n' + 
                         '3 - Clase de IP, Mascara de red, red, Host Local\n' +
                         '4 - Nombre de Maquina, Version OS\n' + 
                         '5 - Opciones 1,3 y 4\n' +
                         '6 - Salir\n\n' + 
                         'Opcion: ')) 
    if opciones == '1':
        os.system('cls')
        infohardlocal()
    elif opciones == '2':
        os.system('cls')
        ultimavezexe()
    elif opciones == '3':
        os.system('cls')
        infored()
    elif opciones == '4':
        os.system('cls')
        nompcveros()
    elif opciones == '5':
        os.system('cls')
        opciones134()
    elif opciones == '6':
        exit()
    else:
        input('\nSeleccion incorrecta. Presione "Enter" para elejir nuevamente.')
        os.system('cls')
        menu()

def infohardlocal():

    print('Info HW Local:\n\n') 
    nombreequipo = platform.node()
    conexion = wmi.connect_server(nombreequipo)
    c = wmi.WMI(wmi = conexion)
    proce = 'Procesador: ' + str(c.Win32_Processor()[0].Name)       
    memram = 'Memoria RAM Total: ' + str(round(int(c.Win32_ComputerSystem()[0].TotalPhysicalMemory) / 1073741824)) + ' GB\n\n'
    for hd in range(len(c.Win32_LogicalDisk())):
        if str(c.Win32_LogicalDisk()[hd].Description) == 'Disco fijo local':
           letrahdd = 'HDD ' + str(hd + 1) + ' - Letra asignada: ' + (c.Win32_LogicalDisk()[hd].DeviceID)
           hddtotal = str(round(int(c.Win32_LogicalDisk()[hd].Size) / 1073741824)) + ' GB'
           hdd = letrahdd + '. Tamaño Total: ' + hddtotal
           print(hdd)
    print(proce)
    print(memram)
    

def ultimavezexe():

    print('Info ultima vez accedido de ...exe (elija el exe):\n\n') 
    programa = input('*****Escriba el nombre exacto del archivo .exe respetando mayúsculas y minúsculas******\n\n' +
                     'Ingrese nombre del archivo .exe: ')#'WINWORD.EXE'#(PRUEBA)
    progmasexe = programa + '.EXE'
    progmasexe2 = programa + '.exe'
    print('\nBuscando archivo, espere por favor')
    info = ''
    encontrado = 0
    for raiz, directorio, archivo in os.walk('C:\\'):
        for arch in archivo:
            if arch == progmasexe:
                ruta = os.path.join(raiz,arch)
                ultimoacceso = (os.popen('dir ' + '"' + ruta + '"' + ' /t:a'))
                for linea in ultimoacceso.readlines():
                        if progmasexe in linea:
                            info = linea.split(' ')
                            encontrado = 1
                            break
            if arch == progmasexe2:
                ruta = os.path.join(raiz,arch)
                ultimoacceso = (os.popen('dir ' + '"' + ruta + '"' + ' /t:a'))
                for linea in ultimoacceso.readlines():
                        if progmasexe2 in linea:
                            info = linea.split(' ')
                            encontrado = 1
                            break
    if encontrado == 1:
        os.system('cls')
        print('Info ultima vez accedido de ...exe(elija el exe)\n\n' +
              'Archivo ' + '"' + programa + '"' + ' encontrado. Ultimo acceso al archivo: ' +
              '\n\nFecha: ' + info[0] + '  Hora: ' + info[2])
    else:
        os.system('cls')
        print('Info ultima vez accedido de ...exe(elija el exe)\n\n' +
              'No se ha encontrado el archivo ' + '"' + programa + '".')
    terminado = input('\n\nOpciones:\n\n' +
                      '1 - Buscar otro archivo\n' +
                      '2 - Menú Principal\n' +
                      '3 - Salir\n\n' +
                      'Opcion: ')
    if terminado == '1':
        ultimavezexe()
    elif terminado == '2':
        os.system('cls')
        menu() 
    elif terminado == '3':
        exit()
                
    
def infored():

    print('Clase de IP, Mascara de red, red, Host Local:\n\n') 
    nombreequipo = platform.node()
    dirip = socket.gethostbyname(nombreequipo) #Se obtiene dirección ip.
    dsplit = dirip.split('.')
    clase = ''
    if int(dsplit[0]) < 128:
        clase = 'Clase A'
    elif int(dsplit[0]) >= 128 and int(dsplit[0]) < 192:
        clase = 'Clase B'
    elif int(dsplit[0]) >= 192 and int(dsplit[0]) < 224:
        clase = 'Clase C'
    elif int(dsplit[0]) >= 224 and int(dsplit[0]) < 240:
        clase = 'Clase D'
    else:
        clase = 'Clase E'
        
    ipconfig = os.popen('ipconfig') #Se ejecuta comando 'ipconfig'.
    mascara = ''
    mascarasp = mascara.split(".")
    for i in ipconfig.readlines():
        if 'subred' in i:
            mascara = i
    masksp = mascara.split(" ")        
    mascarar = masksp[19].replace('\n','') #Se obtiene máscara. 
    masklista = mascarar.split('.')
    #Se convierte la máscara a binario.
    maskbin0 = str(bin(int(masklista[0])).replace('0b',''))
    maskbin1 = str(bin(int(masklista[1])).replace('0b',''))
    maskbin2 = str(bin(int(masklista[2])).replace('0b',''))
    maskbin3 = str(bin(int(masklista[3])).replace('0b',''))
    maskbin = maskbin0 + '.' + maskbin1 + '.' + maskbin2 + '.' + maskbin3
    #Reconoce si el valor es cero, se escribe el valor en el formato '00000000'.
    if maskbin0 == '0':
        maskbin0 = '00000000'
    if maskbin1 == '0':
        maskbin1 = '00000000'
    if maskbin2 == '0':
        maskbin2 = '00000000'
    if maskbin3 == '0':
        maskbin3 = '00000000'
    maskbin = maskbin0 + '.' + maskbin1 + '.' + maskbin2 + '.' + maskbin3
    
    dirip0 = str(bin(int(dsplit[0])).replace('0b',''))
    dirip1 = str(bin(int(dsplit[1])).replace('0b',''))
    dirip2 = str(bin(int(dsplit[2])).replace('0b',''))
    dirip3 = str(bin(int(dsplit[3])).replace('0b',''))
    #Reconoce si el valor es cero, se escribe el valor en el formato '00000000'.
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
    
    diripbinhost = diripreal0 + '.' + diripreal1 + '.' + diripreal2 + '.' + diripreal3 #Se obtiene la direccion ip en el formato 'xxxxxxxx'.'xxxxxxxx'.'xxxxxxxx'.'xxxxxxxx'
                                                                                       #para comparar posteriormente con la dirección de red.
    diripbinhostsp = diripbinhost.split('.')
    
    diripbin = diripreal0 + '.' + diripreal1 + '.' + diripreal2 + '.' + diripreal3 #Se obtiene la direccion ip en el formato 'xxxxxxxx'.'xxxxxxxx'.'xxxxxxxx'.'xxxxxxxx'
    diripbinlist = list((diripbin))
    
    cant1mask = 0
    red = ''
    
    for i in maskbin: 
        if i == '1':
            cant1mask += 1 #Cuenta cantidad de '1' en la máscara.
    cant0mask = 32 - cant1mask #Cantidad de '0' en la máscara            
    host = ''
    host0ant = ''
    
    z = 0
    for d in diripbinlist:
        if z != cant1mask:
            if d != '.':
                red += d
                z += 1
        if z == cant1mask:
            if d != '.':
                host += d

    hostlenres = 32 - len(host)                 
    longredres = 32 - len(red) 
    for cant0resred in range(longredres):
        red += '0'                          #Se completa con '0' la direccion ip en binario sin estar separada por puntos.
    for cant0falt in range(hostlenres):
        host0ant += '0'                     #Se completa con '0' la direccion ip del host en binario sin estar por puntos.
    hostrealbin = host0ant + host
    
    redfinal0 = red[0:8]
    redfinal1 = red[8:16]
    redfinal2 = red[16:24]
    redfinal3 = red[24:32]
    redfinal = [redfinal0, redfinal1, redfinal2, redfinal3] #Red en binario.

    hostfinal0 = hostrealbin[0:8]
    hostfinal1 = hostrealbin[8:16]
    hostfinal2 = hostrealbin[16:24]
    hostfinal3 = hostrealbin[24:32]
    hostfinal = [int(hostfinal0,2), int(hostfinal1,2), int(hostfinal2,2), int(hostfinal3,2)]
    hostfinalpant = list(())
    hostenpantalla = ''
    for hostp in hostfinal:
        if hostp != 0:
            hostfinalpant.append(str(hostp))
            hostfinalpant.append('.')
    hostfinalpantlen = len(hostfinalpant)
    hostfinalrem = hostfinalpant.pop(hostfinalpantlen - 1)


    for hostfp in hostfinalpant:
        hostenpantalla += str(hostfp)
          
    direccionipred = str(int(redfinal[0],2))+ '.' + (str(int(redfinal[1],2)) + '.' + (str(int(redfinal[2],2)) + '.' + (str(int(redfinal[3],2)))))
    direccioniphost = str(int(diripbinhostsp[0],2))+ '.' + (str(int(diripbinhostsp[1],2)) + '.' + (str(int(diripbinhostsp[2],2)) + '.' + (str(int(diripbinhostsp[3],2)))))
    direccioniphostpant = ''
    
    
    if direccionipred == direccioniphost:
        direccioniphostpant = 'La dirección ingresada indica la red'
    else:
        direccioniphostpant = direccioniphost
    
    print('Clase de dirección IP: ' + clase)
    print('Mascara de red: ' + mascarar)
    print('Red: ' + direccionipred)
    print('Host: ' + hostenpantalla)
    print('Direccion ip host: ' + direccioniphostpant + '\n\n')
    

    
def nompcveros():

    print('Nombre de Maquina, Version OS:\n\n')
    nombreequipo = platform.node()
    sistema = platform.system()
    version = platform.version()
    nompc = 'Nombre de equipo: ' + nombreequipo
    sisop = 'Sistema Operativo: ' + sistema + '. Version: ' + version
    print(nompc)
    print(sisop)


def opciones134():

    infohardlocal()
    infored()
    nompcveros()
 

menu()

