#fj的字符串
while True :
    try:
        def Rec_fj(n):
            if n == 1:
                return 'A'
            else:
                return Rec_fj(n - 1) + chr(ord('A')+n-1)+Rec_fj(n-1)
        n = int(input())
        print(Rec_fj(n))
    except:
        break