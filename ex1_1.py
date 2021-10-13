import numpy as np
import doctest
import matplotlib.pyplot as plt
import japanize_matplotlib

def true_function(x):
    '''
    >>> true_function(0)
    0
    '''
    y = np.sin(np.pi * x * 0.8) * 10
    return y

def plot(x_min, x_max):
    dots = 100
    xdata = np.linspace(x_min, x_max, dots)
    ydata = true_function(xdata)
    plt.figure()
    plt.plot(xdata, ydata, label="true_function")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend(loc="best")
    plt.savefig("ex1_1.png")

if __name__ == '__main__':
    doctest.testmod
    x_min = -1
    x_max = 1
    plot(x_min, x_max)