#Sine之舞
while True :
    try:
        def Rec_An(s,n):
            if n == 1:
                return 'sin(1)'
            elif(s == n - 1) and ((n-1) % 2 == 0):
                return 'sin(' + str(n - 1) + '+' +'sin' + str(n) +')'
            elif(s == n - 1) and ((n - 1) % 2 != 0):
                return 'sin(' + str(s) + '-' + Rec_An(s + 1,n) +' )'
            elif s % 2 != 0:
                return 'sin(' + str(s) + '-' + Rec_An(s + 1,n) +')'
            elif s % 2 == 0:
                return 'sin(' + str(s) + '+' + Rec_An(s + 1,n) +')'

        def Rec_Sn(s,n):
            if s == n:
                return Rec_An(1,1) + '+' + str(n)
            else:
                return '(' + Rec_Sn(s + 1,n) + ')' + Rec_An(1,n+1-s) + '+' + str(s)


        n = int(input())
        print(Rec_Sn(1,n) )
    except:
        break