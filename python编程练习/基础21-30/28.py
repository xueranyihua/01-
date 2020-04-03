#哈夫曼树
while True:
    try:
        n = int(input())
        result = 0
        s = list(map(int,input().split()))
        for i in range(n-1):
            s.sort(reverse=True)
            s1 = s.pop()
            s2 = s.pop()
            s.append(s1+s2)
            result += s1+s2
        print(result)
    except:
        break
