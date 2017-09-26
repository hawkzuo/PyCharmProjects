# -*- coding: utf-8 -*-
if __name__ == '__main__':
    # Containers
    l1 = ['r', 'g', 'b', 't', 's', 'v']
    var1 = l1[1:4:1]  # ['g', 'b', 't']
    var2 = l1[1:4:2]  # ['g', 't']
    l1.append('z')
    l1.pop()
    var3 = l1[::-1]  # Reverse
    l1.reverse()
    sorted(l1)  # Sort

    # String
    s1 = 'Normal string'
    s2 = "Double quotes string"

    # Dictionary
    codes = {'p1': 1342, 'p2': 1985}
    # codes.keys() .values() .items()

    # Tuple
    t = ('a', 'b', 3)
    # t[0] t[1] t[2]

    # Set
    s = {'a', 'b', 'c', 'a'}

    # Control flows

    # If statements
    if 'a' == 'a':
        print('str compare by values')

    if 'a' == str('a'):
        print('str on string will not influence values')
    else:
        print('str on string will be two different strings')

    magicNum = 17
    if magicNum < 1:
        print('less than 1')
    elif magicNum < 10:
        print('less than 10')
    else:
        print('greater than 10')

    # for/range
    for i in range(5):
        print(i)  # 01234

    # while/break/continue  C-style
    z = 1 + 1j
    while abs(z) < 100:
        z = z ** 2 + 1
    print(z)

    # ==/is/in
    print(11 == 11.)
    print(11 is 11.)
    print(11 in (11, 22, 33))
