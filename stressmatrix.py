import numpy as np


def strassen_multiply(A, B):
    n = len(A)

    if n == 1:
        return np.dot(A, B)

    A11, A12, A21, A22 = A[:n//2, :n//2], A[:n//2,
                                            n//2:], A[n//2:, :n//2], A[n//2:, n//2:]
    B11, B12, B21, B22 = B[:n//2, :n//2], B[:n//2,
                                            n//2:], B[n//2:, :n//2], B[n//2:, n//2:]

    S1 = B12 - B22
    S2 = A11 + A12
    S3 = A21 + A22
    S4 = B21 - B11
    S5 = A11 + A22
    S6 = B11 + B22
    S7 = A12 - A22
    S8 = B21 + B22
    S9 = A11 - A21
    S10 = B11 + B12
    P1 = strassen_multiply(A11, S1)
    P2 = strassen_multiply(S2, B22)
    P3 = strassen_multiply(S3, B11)
    P4 = strassen_multiply(A22, S4)
    P5 = strassen_multiply(S5, S6)
    P6 = strassen_multiply(S7, S8)
    P7 = strassen_multiply(S9, S10)
    C11 = P5 + P4 - P2 + P6
    C12 = P1 + P2
    C21 = P3 + P4
    C22 = P5 + P1 - P3 - P7

    C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))

    return C

A = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
B = np.array([[17, 18, 19, 20], [21, 22, 23, 24],
             [25, 26, 27, 28], [29, 30, 31, 32]])

result = strassen_multiply(A, B)
print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)
print("\nResult of Strassen's Matrix Multiplication:")
print(result)
