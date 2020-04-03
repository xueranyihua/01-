#阶乘计算
while True:
    try:
        n = int(input())
        for i in range(1,n):
            n = n * i
        print(n)
    except:
        break
