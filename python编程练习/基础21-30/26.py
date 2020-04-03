#报时助手
while True:
    try:
        dic = {0:'zero', 1: 'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten',\
               11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen',\
               19:'nineteen', 20:'twenty',30:'thirty',40:'forty',50:'fifty'}
        s = list(map(int, input().split()))
        res = ''
        if s[0] > 20:
            res += dic[20] + ' '
            res += dic[s[0]%10] + ' '
        else:
            res += dic[s[0]]+' '
        if 10 <= s[1] <= 20:
            res += dic[s[1]]
        else:
            if s[1] == 0:
                res += "o'clock"
            elif s[1]//10 == 0:
                res += dic[s[1]%10]
            elif s[1]//10 == 2:
                res += dic[20] + ' ' + dic[s[1]%10]
            elif s[1]//10 == 3:
                res += dic[30] + ' ' + dic[s[1]%10]
            elif s[1]//10 == 4:
                res += dic[40] + ' ' + dic[s[1]%10]
            elif s[1]//10 == 5:
                res += dic[50] + ' ' + dic[s[1]%10]
        print(res)
    except:
        break
