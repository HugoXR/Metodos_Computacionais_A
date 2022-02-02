import numpy as np


def h(x):
    """Function with returns e^(-x^2/2)/sqrt(2)"""
    return (np.exp(-(x**2)/2)/np.sqrt(2*np.pi))


if __name__ == "__main__":
    xlist = np.linspace(-4, 4, 41)
    hlist = h(xlist)

    print(f"Values of x: {xlist}")
    print(f"Values of h(x): {hlist}")
