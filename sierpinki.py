"""
Sierpinski triangle using Monte Carlo

by Ross Mariano
May 05, 2018
05:39PM
"""
import matplotlib.pyplot as plt
import numpy as np 

def sierpinski(iterations, xStart, yStart, xTri, yTri):
    """
    roll a random number
    if 0,1
        get half distance from last point and A
    if 2,3
        last point and B
    if 4,5
        last point and C
    """
    xLast = xStart
    yLast = yStart
    for i in range(iterations):
        randRoll = np.random.randint(6)
        if randRoll == 0 or randRoll == 1:
            xLast = (xLast + xTri[0])/2
            yLast = (yLast + yTri[0])/2
            plt.scatter(xLast, yLast, color="b", s=5)
        if randRoll == 2 or randRoll == 3:
            xLast = (xLast + xTri[1])/2
            yLast = (yLast + yTri[1])/2
            plt.scatter(xLast, yLast, color="b", s=5)
        if randRoll == 4 or randRoll == 5:
            xLast = (xLast + xTri[2])/2
            yLast = (yLast + yTri[2])/2
            plt.scatter(xLast, yLast, color="b", s=5)
    plt.title("iterations= {}".format(iterations))
    plt.show()

def main():
    # define three random points A,B,C
    # where their x,y values range from 0,1
    # x = [np.random.random_sample() for i in range(3)]
    # y = [np.random.random_sample() for i in range(3)]
    x = [0,1,0.5]
    y = [0,0,1]
    x = np.array(x)
    y = np.array(y)
    plt.scatter(x,y, color="r")

    # set initial positions
    xStart = np.random.random_sample()
    yStart = np.random.random_sample()

    plt.scatter(xStart, yStart, color="g")
    iterations = 1000
    sierpinski(iterations, xStart, yStart, x, y)
    return None

if __name__ == "__main__":
    main()