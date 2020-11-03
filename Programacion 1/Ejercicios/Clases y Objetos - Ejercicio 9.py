class ej9:

    def __init__(self,x):

       self.x = x
        

    def get_string(self):

        z = self.x
        print('Cadena obtenida: ',z)
                
    def print_string(self):

        t = self.x
        h = t.upper()
        print('Cadena en mayúsculas: ',h)
        
x1 = ej9(input('Ingrese texto: '))
x1.get_string()
x1.print_string()

