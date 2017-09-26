import numpy as np
if __name__ == '__main__':
    #
    a = np.array([1, 2, 3, 4])
    print(a)
    print()

    # Vector Operations
    n = 10
    u = np.zeros((n,1))
    print(np.exp(u))
    print()
    for i in range(n):
        u[i] = np.math.exp(u[i])
    print(u)


