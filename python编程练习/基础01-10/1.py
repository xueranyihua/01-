#闰年的判断
while True :
    try:
        n = int(input())
        if n % 4 == 0 and n % 100 != 0:
            print("yes")
        elif n % 400 == 0:
            print("yes")
        else:
            print("no")
    except:
        break