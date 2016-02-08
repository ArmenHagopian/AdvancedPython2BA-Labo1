# Math library
# Author: Sébastien Combéfis
# Version: February 2, 2016
from math import sqrt
def fact(n):
    x = 1
    while n >0:
        x *= n
        n -= 1
    return x
    # """Computes the factorial of a natural number.
    #
    # Pre: -
    # Post: Returns the factorial of 'n'.
    # Throws: ValueError if n < 0
    # """

def roots(a, b, c):
    delta = b**2 - 4*a*c
    try:
        x1 = (b + sqrt(delta))/(2*a)
        x2 = (b - sqrt(delta))/(2*a)
    except:
        return tuple()
    content = x1, x2
    if x1 == x2:
        content = (x1)
    return content
    # """Computes the roots of the ax^2 + bx + x = 0 polynomial.
    #
    # Pre: -
    # Post: Returns a tuple with zero, one or two elements corresponding
    #       to the roots of the ax^2 + bx + c polynomial.
    # """


def integrate(function, lower, upper):
    a = function.split(' ')
    lowResult = 0
    upResult = 0
    i = 0
    while i < len(a):
        number = a[i]
        if number == 'x':
            if a[i+1] == '**':
                exponent = int(a[i+2])
            else:
                exponent = 1

            lowResult += lower**(exponent+1)/(exponent+1)
            upResult += upper**(exponent+1)/(exponent+1)
            
        try:
            type(float(number)) == float
            if a[i-1] == '-':
                lowResult -= int(number)*lower
                upResult -= int(number)*upper
            elif a[i-1] == '+':
                lowResult += int(number)*lower
                upResult += int(number)*upper
        except:
            lowResult += 0
        i += 1

    x = lower
    integral = eval(function)
    x = upper
    integral += eval(function)
    x = (lower+upper)/2
    integral += 4*eval(function)
    integral *= (upper-lower)/6
    print(integral)
    return round(upResult - lowResult, 15)

    # """Approximates the integral of a fonction between two bounds
    #
    # Pre: 'function' is a valid Python expression with x as a variable,
    #      'lower' <= 'upper',
    #      'function' continuous and integrable between 'lower‘ and 'upper'.
    # Post: Returns an approximation of the integral from 'lower' to 'upper'
    #       of the specified 'function'.
    # """


if __name__ == '__main__':
    print(fact(5))
    print(fact(0))

    print(roots(1, 0, 1))
    print(roots(1, 10, 1))
    print(integrate('x ** 2 - 1', -1, 1))
