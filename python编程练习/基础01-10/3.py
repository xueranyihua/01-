#字母图形
while True:
    try:
        n = list(map(int, input().split()))
        s = [['0'  for p in range(max(n)) ]for q in range(max(n))]
        for i in range(n[0]):
            temp1,temp2 = ord('A'), ord('A')
            for j in range(i, n[1]):
                s[i][j] = chr(temp1)
                temp1 += 1
            for k in range(i-1, -1, -1):
                temp2 += 1
                s[i][k] = chr(temp2)
        for x in range(n[0]):
            for y in range(n[1]):
                print(s[x][y],end = '')
            print('')
    except:
        break
