#矩阵乘法
while True:
    try:
        def matrix_mul(matrix1,matrix, n):
            c = [[0 for m1 in range(n)]for m in range(n)]
            for i in range(n):
                for j in range(n):
                    for k in range(n):
                        c[i][j] += matrix1[i][k] * matrix[k][j]
            return c

        n = list(map(int, input().split()))
        s = []
        result = s
        for j in range(n[0]):
            s.append(list(map(int, input().split())))
        if n[1] == 0:
            for i in range(0, n[0]):
                for j in range(0, n[0]):
                    if i == j:
                        result[i][j] = 1
                    else:
                        result[i][j] = 0
        else:
            for k in range(n[1]-1):
                result = matrix_mul(result,s,n[0])
        for i in range(0, result.__len__()) :
            for j in range(0, result[i].__len__()) :
                print(result[i][j],'', end='')
            print('')
    except:
        break
