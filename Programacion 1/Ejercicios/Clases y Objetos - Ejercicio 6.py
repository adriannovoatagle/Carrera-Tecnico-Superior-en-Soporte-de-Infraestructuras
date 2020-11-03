class ej6:

    def __init__(self,x):

        self.x = x
        
    def funcion(self):
        
        n = self.x
        y = list(())
        r = list(())
        for i in n:
            for v in n:
                for z in n:
                    if int(i) + int(z) + int(v) == 0:
                        y.append(i)
                        y.append(v)
                        y.append(z)
                        y.sort()
                        r.sort()
                        if y not in r:
                            r.append(y)
                            y = list(())
                        else:
                            y = list(())
                        
        print('Entrada: ', n,'\nSalida: ',r)
                    

x1 = ej6([-25, -10, -7, -3, 2, 4, 8, 10])
x1.funcion()
