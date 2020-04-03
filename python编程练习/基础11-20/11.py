#十六进制转十进制
while True :
    try:
        s = str(input())[::-1]
        para = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,
                '9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
        result = para[s[0]]
        for  i in range(1,s.__lem__()):
            temp = para[s[i]]*16**i
            result += temp
        print(result)
    except:
        break