# matplotllib is 2D-graphics

from matplotlib import pyplot as plt
import numpy as np

def test_basic_controlled_plotting():
    # Create a figure of size 8x6 inches, 80 dots per inch
    plt.figure(figsize=(8, 6), dpi=80)
    # Create a new subplot from a grid of 1x1
    plt.subplot(1, 1, 1)
    X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    C, S = np.cos(X), np.sin(X)
    # Plot cosine with a blue continuous line of width 1 (pixels)
    plt.plot(X, C, color="blue", linewidth=1.0, linestyle="-", label="cosine")
    # Plot sine with a green continuous line of width 1 (pixels)
    plt.plot(X, S, color="green", linewidth=1.0, linestyle="-", label="sine")


    # Set x limits
    plt.xlim(-4.0, 4.0)     # plt.xlim(X.min() * 1.1, X.max() * 1.1)
    # Set x ticks
    plt.xticks(np.linspace(-4, 4, 9, endpoint=True))    # plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
    # Set y limits
    plt.ylim(-1.0, 1.0)     # plt.ylim(C.min() * 1.1, C.max() * 1.1)
    # Set y ticks
    plt.yticks(np.linspace(-1, 1, 5, endpoint=True))    # plt.yticks([-1, 0, +1],[r'$-1$', r'$0$', r'$+1$'])

    # Legends
    plt.legend(loc='upper left')

    # Annotate example
    # t = 2 * np.pi / 3
    # plt.plot([t, t], [0, np.cos(t)], color='blue', linewidth=2.5, linestyle="--")
    # plt.scatter([t, ], [np.cos(t), ], 50, color='blue')
    # plt.annotate(r'$sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
    #              xy=(t, np.sin(t)), xycoords='data',
    #              xytext=(+10, +30), textcoords='offset points', fontsize=16,
    #              arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
    # plt.plot([t, t], [0, np.sin(t)], color='red', linewidth=2.5, linestyle="--")
    # plt.scatter([t, ], [np.sin(t), ], 50, color='red')
    # plt.annotate(r'$cos(\frac{2\pi}{3})=-\frac{1}{2}$',
    #              xy=(t, np.cos(t)), xycoords='data',
    #              xytext=(-90, -50), textcoords='offset points', fontsize=16,
    #              arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

    # Save figure using 72 dots per inch
    plt.savefig("exercise_2.png", dpi=72)
    # Show result on screen
    plt.show()

def test_figures_subplots_axes_ticks():
    pass



if __name__ == '__main__':
    # Basic Usage
    # X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    # C, S = np.cos(X), np.sin(X)
    # plt.plot(X, C)
    # plt.plot(X, S)
    # plt.show()
    test_basic_controlled_plotting()
    print([0.5,2,4])


    print()