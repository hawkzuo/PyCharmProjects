import numpy as np

# np.dot() => matrix multiplication np.multiply() or * => element-wise multiplication [with broadcasting]



if __name__ == '__main__':
    A = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    x = np.array([1, 2, 3])  # Rank 1 matrix
    print(x.shape)
    print(A.sum(axis=1))
