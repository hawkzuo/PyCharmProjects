import numpy as np
import matplotlib.pyplot as plt

# Why use numpy --> Efficient

if __name__ == '__main__':
    # Basics:

    # Avoid using 1-D arrays
    a = np.array([0, 1, 2, 3])
    b = np.array([[0, 1, 2], [3, 4, 5]])
    c = np.array([[[1], [2]], [[3], [4]]])
    # .ndim     .shape  len()
    assert a.ndim == 1
    assert a.shape == (4,)
    assert len(a) == 4
    assert b.ndim == 2
    assert b.shape == (2, 3)
    assert c.shape == (2, 2, 1)

    # .arange(start, end, step)     linspace(start, end, numPts, includingEndpoint)
    a = np.arange(10)
    print(a)
    # Use tuples of coordinates to access each cell
    assert (a[0], a[2], a[-1]) == (0, 2, 9)
    a = np.diag(np.arange(3))
    assert a[1, 1] == 1

    b = np.arange(1, 9, 2)
    print(b)
    c = np.linspace(0, 1, 6)
    print(c)
    d = np.linspace(0, 1, 5, endpoint=False)
    print(d)

    # Common arrays
    a = np.ones((3, 3))
    b = np.zeros((2, 2))
    c = np.eye(3)
    d = np.diag(np.array([1, 2, 3, 4]))
    print(a, '\n', b, '\n', c, '\n', d)

    # Random numbers
    a = np.random.rand(4)  # uniform in [0, 1]
    b = np.random.randn(4)  # Gaussian
    np.random.seed(1234)

    # Data type, 'float64' is the default data type, other types such as 'int64' 'complex128' 'bool'
    c = np.array([1, 2, 3], dtype=float)
    assert c.dtype == 'float64'
    f = np.array(['Bonjour', 'Hello', 'Hallo', ])
    assert f.dtype == '<U7'

    # Basic Plotting
    print('Basic Plotting')
    x = np.linspace(0, 3, 20)
    y = np.linspace(0, 9, 20)
    # plt.plot(x, y)
    # # Must use .show() if not in iPython environment
    # plt.show()
    # plt.plot(x, y, 'o')

    print('Copies and views')
    a = np.arange(10)
    b = a[::2]  # b is view of a
    c = a[::2].copy()  # force a copy
    assert np.may_share_memory(a, b) == True
    assert np.may_share_memory(a, c) == False
    b[0] = 12
    print(a)




    # Operations:
    # All arithmetic operates element-wise
    # Scalars will be broadcasting automatically
    # Use np.array_equal() to compare arrays
    # np.logical_or[and](a)    np.sin(a)    np.log(a)    np.exp(a)
    # a.T is a view of a

    # np.sum(a)
    x = np.array([[1, 1], [2, 2]])
    print(x)
    print(x.sum(axis=0)) # columns (first dimension)
    assert x[:, 0].sum(), x[:, 1].sum() == (3, 3)
    print(x.sum(axis=1))  # rows (second dimension)
    assert x[0, :].sum(), x[1, :].sum() == (2, 4)
    # a.min() a.max() a.argmin() a.argmax() a.mean() np.median(a) a.std()
    # np.median(y, axis=-1) # last axis

    # dimension shuffling
    # flatten / ravel       reshape         transpose

