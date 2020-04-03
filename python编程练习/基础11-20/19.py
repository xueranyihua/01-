#完美代价
while True:
    try:
        def huiwen(n, s):  # 判断能不能组成回文数
            temp = set()
            if n % 2 == 0:
                for i in range(26):
                    if s.count(chr(ord('a') + i)) % 2 != 0:  # 如果某个字符不是偶数个
                        print('Impossible')
                        return False
                else:
                    return True

            else:
                for j in range(26):
                    if s.count(chr(ord('a') + j)) % 2 != 0:
                        temp.add(chr(ord('a') + j))  # 把个数是奇数个的字符放进temp
                    if len(temp) > 1:
                        print('Impossible')
                        return False
                else:
                    return True


        def step(n, s, s1, res):
            for i in range(n // 2):
                if s[i:].count(s[i]) != 1:
                    temp = s1[:n - i].index(s[i])  # 是要移动的步数
                    s1.pop(temp)
                    res += temp
                    s = s1[::-1]
                else:
                    res += n // 2 - i
                    s[i] = None
                    s1 = s[::-1]
            return res


        n = int(input())
        s = list(input())
        s1 = s[::-1]
        res = 0
        if huiwen(n, s):
            print(step(n, s, s1, res))
    except:
        break
