import numpy as np
from GaussJordanInverse import gaussJordanInverse

np.set_printoptions(precision=10)

class Matrix:

    def __init__(self, A):
        self.__M = A

    # RETURNS THE DETERMINANT OF A MATRIX
    def Det(self):
        det = 0.0
        for i in range(0, self.__M.shape[1]):
            positive = 1.0
            negative = 1.0
            for j in range(0, self.__M.shape[0]):
                k = j + i
                l = i - j
                if k > (self.__M.shape[1] - 1):
                    k = k - self.__M.shape[0]
                if l < 0:
                    l = self.__M.shape[0] + l
                positive *= self.__M[j, k]
                negative *= self.__M[j, l]
            det += positive
            det -= negative
        return det

    # RETURNS THE 1-NORM OF A MATRIX
    def OneNorm(self):
        cols = []
        for i in range(0, self.__M.shape[1]):
            sum = 0.0
            for k in range(0, self.__M.shape[0]):
                if self.__M[k, i] < 0:
                    sum += self.__M[k, i] * -1
                else:
                    sum += self.__M[k, i]
            cols.append(sum)
        return max(cols)

    # RETURNS THE INFINITY-NORM OF A MATRIX
    def InfNorm(self):
        rows = []
        for i in range(0, self.__M.shape[0]):
            sum = 0.0
            for k in range(0, self.__M.shape[1]):
                if self.__M[i, k] < 0:
                    sum += self.__M[i, k] * -1
                else:
                    sum += self.__M[i, k]
            rows.append(sum)
        return max(rows)

    # RETURNS THE CONDITION NUMBER BASED ON THE 1-NORM
    def ConditionNumOne(self):
        InvM = Matrix(gaussJordanInverse(self.__M))
        one_norm = self.OneNorm()
        one_norm_inv = InvM.OneNorm()
        con_num = one_norm * one_norm_inv
        return con_num

    # RETURNS THE CONDITIONS NUMBER BASED ON THE INFINITY-NORM
    def ConditionNumInf(self):
        InvM = Matrix(gaussJordanInverse(self.__M))
        inf_norm = self.InfNorm()
        inf_norm_inv = InvM.InfNorm()
        con_num = inf_norm * inf_norm_inv
        return con_num

# Solving the example
if __name__ == "__main__":
    B = np.array([[3.50, 2.77, -0.76, 1.80], [-1.80, 2.68, 3.44, -0.09],
              [0.27, 5.07, 6.90, 1.61], [1.71, 5.45, 2.68, 1.71]])
    print("B =\n", B)
    N = Matrix(B)
    print("detB =\n", round(N.Det(), 10))
    print("Condition num based on 1 norm --> ", round(N.ConditionNumOne(), 10))
    print("Condition num based on inf norm --> ", round(N.ConditionNumInf(), 10))
