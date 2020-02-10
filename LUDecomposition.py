#ライブラリのインポート
import numpy as np
from random import randint

#LU分解したいn * n行列を入力
n = 3
#Aはサンプル．分解したい行列を入力
A = np.array([[randint(1,10) for j in range(0, n)] for i in range(0,n)]).astype(np.float)
print(A);print()

class LUClass:
    def __init__(self, matrix):
        self.row = len(matrix)
        self.matrix = matrix
    
    def Disassemble(self):
        #初期LU行列の生成
        row = self.row
        matrix = self.matrix
        U = np.identity(n = row, dtype = float) #全て0にするとZeroDividionErrorが怖いので単位行列に
        L = np.identity(n = row, dtype = float)
        #LU分解のアルゴリズムはここから
        for k in range(0, row):
            for j in range(k, row):
                U[k][j] = matrix[k][j] - (sum(L[k][s] * U[s][j] for s in range(0, row) if s != k))
                if j == k:
                    w = 1 / U[k][k]
            for i in range(k + 1, row):
                L[i][k] =  w * (matrix[i][k] - sum(L[i][s] * U[s][k] for s in range(0, row) if s != k))
        return (L, U)

K = LUClass(A)
L, U = K.Disassemble()
print(L);print();print(U);print()
print(np.dot(L, U))