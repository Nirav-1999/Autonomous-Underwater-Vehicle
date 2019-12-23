lower = -10
higher = 10


def xturn(read_x):
    if(read_x < lower):
        #increase right motor speed
        #read new value(read_newx)
        xturn(read_newx)
    elif(read_x > higher):
        #increase left motor speed
        #read new value(read_newx)
        xturn(read_newx)
    else:
        return 

