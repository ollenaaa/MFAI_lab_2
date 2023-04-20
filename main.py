import random
import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

# межі інтегрування
a = 1
b = 2

# кількість точок
num_points = 10000


# головна та тестова функції в яких треба обчислити інтеграл
def f(x, function='main'):
    if function == 'main':
        return np.exp(x**2)
    elif function == 'test':
        return x ** 2 + 2 * x + 3


# генерація випадкових точок
def random_point(function):
    x = random.uniform(a, b)
    y = random.uniform(0, max([f(x, function) for x in [1, 2]]))
    return x, y


# обчислення інтегралу методом монте-карло
def monte_carlo_integration(function):
    points_under_curve = []
    points_above_curve = []
    sum = 0
    for i in range(num_points):
        x, y = random_point(function)
        if y <= f(x, function):
            sum += 1
            points_under_curve.append((x, y))
        else:
            points_above_curve.append((x, y))

    integral = (b - a) * max(f(np.array([a,b]), function)) * sum / num_points
    return integral, points_under_curve, points_above_curve


# похибки
def find_errors(function, integral):
    true_integral = quad(lambda x: f(x, function), a, b)[0]
    absolute_error = abs(true_integral - integral)
    relative_error = absolute_error / true_integral
    print('absolute error of', function, 'function = ', absolute_error)
    print('relative error of', function, 'function = ', relative_error)
    return absolute_error, relative_error


def print_(function, points_under_curve, points_above_curve):
    x1_points = [point[0] for point in points_under_curve]
    y1_points = [point[1] for point in points_under_curve]
    x2_points = [point[0] for point in points_above_curve]
    y2_points = [point[1] for point in points_above_curve]

    fig, ax = plt.subplots()

    ax.set_title('Monte Carlo Integration of ' + function + ' function')
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    ax.scatter(np.linspace(a, b, 100), f(np.linspace(a, b, 100), function), s=1, c='black')
    ax.scatter(x1_points, y1_points, s=1, c='grey')
    ax.scatter(x2_points, y2_points, s=1, c='green')

    plt.show()


integral, main_points_under_curve, main_points_above_curve = monte_carlo_integration('main')
test_integral, test_points_under_curve, test_points_above_curve = monte_carlo_integration('test')

print('monte carlo approximation of main function = ', integral)
find_errors('main', integral)

print('monte carlo approximation of test function = ', test_integral)
find_errors('test', test_integral)

print_('main', main_points_under_curve, main_points_above_curve)
print_('test', test_points_under_curve, test_points_above_curve)


