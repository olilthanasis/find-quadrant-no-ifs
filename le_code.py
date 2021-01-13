def quad(x,y):
    return (not((x>0) and (y>0)) and not (y>0))*2 + ((x>0) != (y>0)) + 1
