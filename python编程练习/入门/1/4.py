#Fibonacci数列解析链
while True :
    try:
        n = int(input())
        res1,res2 = 1,1
        for i in range(3,n+1):
            res1 ,res2 = res2 %10007,(res1 +res2 )%10007
        print(res2)
    except:
        break