#圆的面积
import math
while True :
    try:
        r = float(input())
        s = math.pi*r*r
        print("{:.7f}".format(s))    #{:.7f}标是保留小数点后7位小数
    except:
        break