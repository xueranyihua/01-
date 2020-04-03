#高精度加法
while True:
    try:
        a = input()
        b = input()
        A = a.rjust(max(len(a),len(b)), '0')
        B = b.rjust(max(len(a),len(b)), '0')
        c = []
        temp = 0
        for i in range(len(A)-1, -1, -1):
            c.append((int(A[i]) + int(B[i]) + temp) % 10)
            if (int(A[i]) + int(B[i])+temp) >= 10:
                temp = (int(A[i]) + int(B[i]) + temp) // 10
            else:
                temp = 0
        if temp == 0:
            pass
        else:
            c.append(temp)
        for x in c[::-1]:
            print(x,end = '')
    except:
        break
