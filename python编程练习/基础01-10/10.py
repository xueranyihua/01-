#十进制转十六进制
while True:
    try:
        n = int(input())
        print(hex(n)[2:].upper())
        break
    except:
        break