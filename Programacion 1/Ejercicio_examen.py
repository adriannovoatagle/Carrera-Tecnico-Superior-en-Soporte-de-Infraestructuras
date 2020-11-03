def sumatoria():

    r = 0
    try:
        n = int(input('Ingrese un numero: '))
        m = int(input('Ingrese otro numero: '))
         
        if int(m) > int(n):
            for i in range(n,m + 1):
                if int(i) % 2 == 0:
                    r += int(i)
        if int(n) > int(m):
            for i in range(m,n + 1):
                if int(i) % 2 == 0:
                    r += int(i)
        if n == m:
            if int(n) % 2 == 0:
                r = int(n)
    except ValueError:
        input('Uno o ambos datos no son un numero. Presione una tecla para intentar nuevamente.')
        sumatoria()
        
    print('Sumatoria n° pares = ' + str(r))

sumatoria()
