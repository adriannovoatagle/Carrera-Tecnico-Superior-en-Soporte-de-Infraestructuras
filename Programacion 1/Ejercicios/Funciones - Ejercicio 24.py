def txt():
    x = open("texto.txt",'r')
    z = list(())
    for i in x:
        z += i.split(' ')
    print(z)
txt()
    
    
