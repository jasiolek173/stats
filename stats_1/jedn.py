import math
from random import gauss

import matplotlib.pyplot as plt
from numpy import arange
from numpy import log
from numpy.random import seed


class AnalyticalNormal:
    def __init__(self, oczek, war):
        self.oczek = oczek
        self.war = war

    def calculate(self):
        start = -3.5 * self.war
        stop = 3.5 * self.war
        step = 0.01

        x = []
        y = []
        i = start
        while i <= stop:
            x.append(i)
            y.append(self.get_value(i))
            i += step

        return x, y

    def get_value(self, x):
        return 1 / (self.war * math.sqrt(2.0 * math.pi)) * math.exp(
            -math.pow(x - self.oczek, 2) / (2 * math.pow(self.war, 2))
        )

    def plot(self, x, y):
        # plt.figure()
        plt.plot(x, y)
        plt.grid()
        plt.show()


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return "[" + str(self.x) + "," + str(self.y) + "]"


def create_list_of_points(x):
    seed(1)
    list_of_points = []
    for _ in range(x):
        list_of_points.append(Point(gauss(0, 1), gauss(0, 1)))
    return list_of_points


def change_to_y(points):
    return list(
        map(lambda p: Point(((-2 * log(p.distance_from_origin() ** 2)) ** 0.5) * p.x / p.distance_from_origin(),
                            ((-2 * log(p.distance_from_origin() ** 2)) ** 0.5) * p.y / p.distance_from_origin()),
            points))


if __name__ == "__main__":
    values = create_list_of_points(50000)
    values = list(filter(lambda x: x.distance_from_origin() <= 1, values))
    print(len(values))
    for i in values:
        print(i)
    values = change_to_y(values)
    print(len(values))
    for i in values:
        print(i)
    tog = []
    for p in values:
        tog.append(p.x)
        tog.append(p.y)

    print(len(tog))
    plt.figure()
    plt.hist(tog, density=True, bins=arange(-3.5, 3.5, 0.1))
    plt.ylabel('Probability')
    # plt.plot(x_axis, y_axis, 'r')
    # plt.show()

    analytics = AnalyticalNormal(0, 1)
    x, y = analytics.calculate()
    analytics.plot(x, y)
