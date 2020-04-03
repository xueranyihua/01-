#杨辉三角
while True :
    try:
        n = int(input() )
        s = [[0 for i in range(n)] for j in range(n)]
        for num in range(n):
            s[num][0] = 1
        for i in range(n):
            for j in range(i+1):
                s[i][j] = s[i - 1][j - 1] + s[i - 1][j]
        for i in range(n):
            for j in range (n):
                if s[i][j] != 0:
                    print(s[i][j],'  ',end = '')
            print('')

    except:
        break