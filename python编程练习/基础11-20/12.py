#十六进制转八进制
while True :
    try:
        n = int(input())
        for i in range(n):
            s = int(input() ,16)   #十六进制转为十进制
            result = oct(s)  #oct为内建函数，十进制转为八进制
    except:
        break