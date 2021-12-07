import numpy as np
import copy
np.set_printoptions(precision=10)

''' CALCULATES THE INVERSE OF A NON-SINGULAR MATRIX USING GAUSS-JORDAN ELIMINATION METHOD '''
def gaussJordanInverse(A):
    n = A.shape[0]
    a = copy.deepcopy(A)
    B = np.zeros((A.shape[0], A.shape[1]), float)
    np.fill_diagonal(B, 1)

    # Elimination Phase lower part
    for k in range(0, n - 1):
        for i in range(k + 1, n):
            if a[i, k] != 0.0:
                if a[k, k] == 0:
                    tempA = copy.deepcopy(a[i, 0:a.shape[1]])
                    a[i, 0:a.shape[1]] = a[k, 0:a.shape[1]]
                    a[k, 0:a.shape[1]] = tempA
                    tempB = copy.deepcopy(B[i, 0:B.shape[1]])
                    B[i, 0:B.shape[1]] = B[k, 0:B.shape[1]]
                    B[k, 0:B.shape[1]] = tempB
                else:
                    lam = a[i, k] / a[k, k]
                    a[i, k:n] = a[i, k:n] - lam * a[k, k:n]
                    B[i, 0:B.shape[1]] = B[i, 0:B.shape[1]] - lam * B[k, 0:B.shape[1]]

    # Elimination Phase upper part
    for k in range(n - 1, 0, -1):
        for i in range(k - 1, -1, -1):
            if a[i, k] != 0.0:
                if a[k, k] == 0:
                    tempA = copy.deepcopy(a[i, 0:a.shape[1]])
                    a[i, 0:a.shape[1]] = a[k, 0:a.shape[1]]
                    a[k, 0:a.shape[1]] = tempA
                    tempB = copy.deepcopy(B[i, 0:B.shape[1]])
                    B[i, 0:B.shape[1]] = B[k, 0:B.shape[1]]
                    B[k, 0:B.shape[1]] = tempB
                else:
                    lam = a[i, k] / a[k, k]
                    a[i, k:n] = a[i, k:n] - lam * a[k, k:n]
                    B[i, 0:B.shape[1]] = B[i, 0:B.shape[1]] - lam * B[k, 0:B.shape[1]]

    # Back substitution
    for i in range(0, n):
        B[i, 0:B.shape[1]] = B[i, 0:B.shape[1]] / a[i, i]

    return B

# Solving the example
if __name__ == "__main__":
    A = np.array([[2.0, -1.0, 0.0], [-1.0, 2.0, -1.0], [0.0, -1.0, 2.0]])
    riversed_A = gaussJordanInverse(A)
    print("ans = \n", riversed_A)
