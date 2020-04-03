#分解质因数
while True:
    try:
        def zhishufenjie(res, n ,result):    #result字典
            for i in range(2, n+1):
                if n % i == 0:
                    res += str(i)
                    n = n // i
                    if n == 1:
                        return res
                    elif n in result.keys():
                        res += '*'
                        res += result[n]
                        return res
                    else:
                        res += '*'
                        return zhishufenjie(res,n,result )
        min_num, max_num = map(int,input() .split() )
        result = {}
        for num in range(min_num ,max_num + 1):
            res = ''
            result[num] = zhishufenjie(res ,num ,result )
        for k,v in result .items() :
            s = str (k) + '=' +str(v)
            print(s)

    except:
        break