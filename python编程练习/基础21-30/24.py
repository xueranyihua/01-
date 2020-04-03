#龟兔赛跑预测
import math
while True :
    try:
        v1,v2,t,s,l = map(int,input().split() )
        x1,x2 = 0,0     #x1,x2标识兔子和乌龟走过的路程
        time = 0
        for i in range(math.ceil(l/v2) ):
            x1 += v1
            x2 += v2
            time  += 1
            if x1 >= 1 and x2 < x1:
                print('R')
                print(time)
                break
            elif x1 < x2 and x2 >= x1:
                print('T')
                print(time)
                break
            elif x1 == x2 >= l:
                print('D')
                print(time)
                break
            if (x1 - x2) >= t:
                x2 += v2 * s
                time += s
            if x1 >= l and x2 < x1:
                print('R')
                print(time)
                break
            elif x1 < x2 and x2 >= l:
                print('T')
                print(math.ceil(l / v2))
                break
            elif x1 == x2 and x2 >= l:
                print('D')
                print(time)
                break

    except:
        break