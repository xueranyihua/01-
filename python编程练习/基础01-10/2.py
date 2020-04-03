#0  1 字串
while True :
    try:
        for i in range(32):
            print(str(bin(i))[2:].rjust(5,'0') )
        break 
    except:
        break