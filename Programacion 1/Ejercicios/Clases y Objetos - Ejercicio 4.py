class subc:

    def __init__(self,x):

        self.x = x

    def funcion(self):

        d = self.x
        v = list(())
        y = list(())
        r = list(())
        r.append(v)
        for i in d:
            y.append(i)
            if i not in r:
                r.append(y)
                y = list(())
        for i in d:
            for z in d:
                if i != z:
                    y.append(z)
                    if y not in r:                    
                        r.append(y)
                        y = list(())       

        r.append(d)
        print ('Los subconjuntos posibles son: ',r)

x1 = subc (list((str(input('Ingrese numeros: ')))))
x1.funcion()
