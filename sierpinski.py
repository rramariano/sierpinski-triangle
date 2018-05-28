"""
Sierpinski triangle simulation

by Ross Mariano
May 05, 2018
05:39PM
"""
import matplotlib.pyplot as plt
import numpy as np 

def sierpinski(iterations, xStart, yStart, xTri, yTri):
    """
    roll a random number

    if 0
        get half distance from last point to point 0
    if 1
        get half distance from last point to point 1
    if 2
        get half distance from last point to point 2
    """
    xLast = xStart
    yLast = yStart

    for i in range(iterations):
        randRoll = np.random.randint(3)
        xLast = (xLast + xTri[randRoll])/2
        yLast = (yLast + yTri[randRoll])/2
        plt.scatter(xLast, yLast, color="b", s=5)

    plt.title("iterations= {}".format(iterations))
    plt.show()

def main():
    # define 3 random points
    # where their x,y values range from 0,1
    x = [np.random.random_sample() for i in range(3)]
    y = [np.random.random_sample() for i in range(3)]

    x = np.array(x)
    y = np.array(y)
    plt.scatter(x,y, color="r")

    # set initial positions
    xStart = np.random.random_sample()
    yStart = np.random.random_sample()

    plt.scatter(xStart, yStart, color="g")
    iterations = 2000
    sierpinski(iterations, xStart, yStart, x, y)
    return None

if __name__ == "__main__":
    main()
