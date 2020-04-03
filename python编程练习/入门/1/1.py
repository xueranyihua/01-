#A+B之和
while True :
    try:
        s = list(map(int,input().split()))
        print(sum(s))
    except:
        break