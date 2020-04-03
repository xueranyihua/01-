#数的读法
while True:
    try:
        s = {0: 'ling', 1: 'yi', 2: 'er', 3: 'san', 4: 'si', 5: 'wu', 6: 'liu', 7: 'qi', 8: 'ba', 9: 'jiu'}
        res = []
        long_data = input()

        def read_four_num(n):   #用这个函数读四位数
            temp = list(map(int, n))
            if temp[0] != 0:   #千位如果是零不读
                res.append(s[temp[0]])
                res.append('qian')
            else:
                pass

            if temp[1] != 0:    #百位不为零直接读出来
                res.append(s[temp[1]])
                res.append('bai')
            elif (temp[0] == 0 and temp[1] == 0) or (temp[1] == 0 and temp[2] == 0 and temp[3] == 0):   #千位，百位都是零的话不读
                pass
            else:
                res.append(s[temp[1]])    #千位不是零，百位是零读出来

            if temp[2] != 0 and temp[2] != 1:    #十位不是零和一
                res.append(s[temp[2]])
                res.append('shi')
            elif temp[2] == 1 and temp[0] == 0 and temp[1] == 0:
                res.append('shi')
            elif (temp[1] == 0 and temp[2] == 0) or (temp[2] == 0 and temp[3] == 0):   #如果百位是零，十位也是零，连零读一个
                                                                                       #如果百位个位都是零，不读
                pass
            else:
                res.append(s[temp[2]])

            if temp[3] != 0:
                res.append(s[temp[3]])
            else:
                pass
            return res
        if 0 < len(long_data) <= 4:
            ans = read_four_num(long_data.rjust(4,'0'))
        elif 4 < len(long_data) <= 8:
            new = long_data.rjust(8,'0')
            read_four_num(new[:4])
            res.append('wan')
            if new[4:] != '0000' and new[4:][0] == '0':
                res.append('ling')
            ans = read_four_num(new[4:])
        elif 8 < len(long_data) <= 10:
            new = long_data.rjust(12,'0')
            read_four_num(new[:4])
            res.append('yi')
            if new[4:8] != '0000':
                read_four_num(new[4:8])
                res.append('wan')
            elif new[4:12] == '00000000':
                pass
            else:
                res.append('ling')
            ans = read_four_num(new[8:12])
        for x in ans:
            print(x,'',end= '')
    except:
        break
