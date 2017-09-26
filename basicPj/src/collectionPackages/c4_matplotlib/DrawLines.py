import matplotlib.pyplot as plt
import numpy as np
import sympy

def my_lines(ax, pos, *args, **kwargs):
    if ax == 'x':
        for p in pos:
            plt.axvline(p, *args, **kwargs)
    else:
        for p in pos:
            plt.axhline(p, *args, **kwargs)





if __name__ == '__main__':
    # data1 = [1,1,1,0,0,   0,1,0,1,1,     1,1,1,1,0,     1,0,1,0,1,      1]
    # dt = np.repeat(data1, 2)
    # t = 0.5 * np.arange(len(dt))
    # nrzi = np.array([0,1,1,0,0,1,1,1,1,1,   1,1,1,0,0,0,0,1,1,0,    0,1,1,0,0,1,1,0,0,0,    0,1,1,1,1,0,0,0,0,1,    1,1])
    # # bits = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0]
    # # data = np.repeat(bits, 2)
    # # clock = 1 - np.arange(len(data)) % 2
    # # manchester = 1 - np.logical_xor(clock, data)
    # # t = 0.5 * np.arange(len(data))
    #
    # plt.hold(True)
    # my_lines('x', range(20), color='.5', linewidth=2)
    # my_lines('y', [0.5, 2.5], color='.5', linewidth=2)
    # # plt.step(t, clock + 4, 'r', linewidth=2, where='post')
    # plt.step(t, dt + 2, 'r', linewidth=2, where='post')
    #
    # plt.step(t, nrzi, 'r', linewidth=2, where='post')
    # plt.ylim([-1, 4])
    # plt.xlim([0,20])
    # #
    # count = 0
    # for tbit, bit in enumerate(data1):
    #     if count > 19:    #         break
    #     plt.text(tbit + 0.5, 1.25, str(bit))
    #     count += 1
    #
    # plt.gca().axis('off')
    # plt.gca().set_aspect('equal', adjustable='box')
    # plt.show()

    from sympy.abc import x
    from sympy.plotting import plot
    f1 = sympy.functions.special.delta_functions.DiracDelta(x, 1)
    # f2 = sympy.functions.special.delta_functions.DiracDelta(x, -1)
    plot(f1)

