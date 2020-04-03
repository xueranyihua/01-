#数列的特征
while True :
    try:
        n = int(input())
        s = list(map(int,input().split() ))
        print(min(s ))
        print(max(s ))
        print(sum(s ))
    except:
        break