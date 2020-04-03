#查找整数
while True :
    try:
        n = int(input())
        s = list(map(int,input() .split() ))
        n1 = int(input() )
        if n1 is s:
            print(int(s.index(n1)) +1)
        else:
            print(-1)
    except:
        break