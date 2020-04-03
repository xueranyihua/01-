#数列排序
while True :
    try:
        n = int(input())
        s = sorted(list(map(int,input().split())))
        for i in s:
            print(i,'',end= '')
    except:
        break