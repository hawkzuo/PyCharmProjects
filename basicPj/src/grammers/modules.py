# Scripts & modules => Code reusing
# To use package 'scipy' on Windows, the interpreter must be Anaconda3
import os
from os import listdir
import numpy as np
import scipy
from pylab import *

# Sometimes we want code to be executed when a module is run directly, but not when it is imported by another
# module. if __name__ == ’__main__’ allows us to check whether the module is being run directly.

if __name__ == '__main__':
    print(os.listdir('.'))
    print(listdir('..'))
    print(np.linspace(0, 10, 6))
    print(scipy.__version__)

