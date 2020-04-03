#特殊的数字
while True :
    try:
        for num in range(100,1000):
            bai = (num // 100)*(num // 100)*(num)//100
            shi = (num % 100 // 10)*(num % 100 // 10)*(num % 100 // 10)
            ge = (num % 100 % 10)*(num %100 % 10)*(num % 100 % 10)
            if bai + shi + ge == num:
                print(num)
        break
    except:
        break