def ed():
    x = list((str(12311)))
    y = list(())
    c = ''
    for i in x:
        c = x.count(i)
        if c == 1:
            y.append(i)
    return y
    
print(ed())
    


    
