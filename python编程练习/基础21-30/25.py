#回型取数
import math
while True:
    try:
        m, n = map(int,input().split())
        res = []
        for i in range(0,m):
            res.append(input().split())
        N = math.ceil(min(m,n)/2)
        result = []
        num = 0
        for loop in range(N):
            for x in range(loop,m-loop):
                result.append(res[x][loop])
            for y in range(loop+1,n-loop):
                result.append(res[m-1-loop][y])
            if n-1 > 2*loop:
                for p in range(m-loop-2,loop-1,-1):
                    result.append(res[p][n-1-loop])
            if m-1 > 2*loop:
                for q in range(n-loop-2,loop,-1):
                    result.append(res[loop][q])
        for x in result:
            print(x,'',end='')
    except:
        break
