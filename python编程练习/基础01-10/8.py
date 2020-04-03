#回文数&特殊回文数
while True :
    try:
        n = int(input() )
        for num in range(10000,1000000):
            temp = str(num)
            if temp[0:] == temp[::-1]:  #判断是否是回文数
                if sum(list(map(int,temp))) == n:
                    print(num)
        break
    except:
        break