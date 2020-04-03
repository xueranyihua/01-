#时间转换
while True :
    try:
        t = int(input())
        h = t // 3600
        m = t%3600 // 60
        s = t % 3600 %60
        print(str(h)+':'+str(m)+':'+str(s))
    except:
        break