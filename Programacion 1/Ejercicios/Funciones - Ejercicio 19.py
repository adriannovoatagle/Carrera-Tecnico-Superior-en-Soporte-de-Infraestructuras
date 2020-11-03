def elimina():
    x = [1,2,3,4]
    y = list(())
    for i in x:
        x.pop()
        x.reverse()
        x.pop()
        x.reverse()
        y = x
        return y

print (elimina())