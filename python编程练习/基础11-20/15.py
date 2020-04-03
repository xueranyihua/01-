#字符串对比
while True :
    try:
        s1 = input()
        s2 = input()
        if len(s1) != len(s2):
            print(1)
        elif s1 == s2:
            print(2)
        else:
            for i in range(s1.__len__()):
                if s1[i] == s2[i] or ord(s1[i]) + 32 == ord(s2[i]) or ord(s1[i]) - 32 == ord(s2[i]):
                    flag = 0
                else:
                    flag = 1
                    print(4)
                    break
        if flag == 0:
            print(3)
    except:
        break