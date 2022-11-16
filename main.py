"""
MIT License

Copyright (c) 2022 Yaroslav Svitlytskyi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import types
import typing
from functools import cache


@cache
def get_factorial(n: int) -> int:
    """

    Example of usage:
    * get_factorial(5) -> 120
    """

    return 1 if n == 0 else n * get_factorial(n - 1)


def get_fibonacci(n: int) -> float:
    """

    Example of usage:
    * get_fibonacci(10) -> 55
    """

    a = 0
    b = 1
    i = 0
    while i <= n - 2:
        c = a + b
        a = b
        b = c

        i += 1
    return b


def get_quick_pow(a: float, n: int) -> float:
    """

    Example of usage:
    * get_quick_pow(2, 2) -> 4
    """

    w = 1
    while n != 0:
        if n % 2 == 1:
            w *= a
        a = a * a
        n //= 2
    return w


def secant_method(f: types.FunctionType, start: int, end: int, eps: int) -> float:
    """

    Example of usage:
    * secant_method(lambda x: x ** 2 - 2, 1, 3, 0.00000001) -> 1.4142...
    """

    c = 0
    while True:
        if f(start) == f(end):
            break

        c = start - (end - start) * f(start) / (f(end) - f(start))
        start = end
        end = c

        fc = f(c)
        if fc < 0:
            fc *= - 1
        if fc < eps:
            break
    return c


def bisection_method(f: types.FunctionType, start: float, end: float, eps: float) -> float:
    """

    Example of usage:
    * bisection_method(lambda x: x ** 2 - 2, 0.1, 2, 0.0001) -> 1.4142...
    """

    if start == 0:
        return start
    if end == 0:
        return end
    while True:
        s = (start + end) / 2
        if f(s) == 0:
            return s
        if f(s) * f(start) < 0:
            end = s
        else:
            start = s
        distance = end - start
        if distance <= 0:
            distance *= -1
        if distance < eps:
            break
    return (start + end) / 2


def get_sqrt_by_newton_method(x: int, eps: int) -> float:
    """

    Example of usage:
    * get_sqrt_by_newton_method(2, 0.0001) -> 1.4142...
    """

    a = 1
    b = x
    while True:
        a = (a + b) / 2
        b = x / a
        difference = b - a
        if difference < 0:
            difference *= -1
        if difference < eps:
            break
    return (a + b) / 2


def get_area_by_trapezoidal_rule(
        f: typing.Any,
        start: float,
        end: float,
        n: typing.Union[int]) -> float:
    """

    Example of usage:
    * get_area_by_trapezoidal_rule(math.sin, 0, math.pi, 10000) -> 1.99999....
    """

    s = 0
    h = (end - start) / n
    prev_fb, prev_ffb = None

    for i in range(n):
        if prev_fb is None:
            fa = start + h * i
        else:
            fa = prev_fb

        fb = start + h * (i + 1)
        prev_fb = fb

        if prev_ffb is None:
            ffa = f(fa)
        else:
            ffa = prev_ffb

        ffb = f(fb)
        prev_ffb = ffb

        s += (ffa + ffb) / 2 * h
    return s


def get_1_difference_value(f: types.FunctionType, x: float, dx: float) -> float:
    """

    Example of usage:
    * get_difference_value(lambda x: x ** 2 - 2, 1, 0.000001) -> 2.0000....
    * get_difference_value(math.sin, 1, 0.000001) -> 0.54....

    !Important information:
    The best delta x is 0.000001 for every case
    """

    fa = f(x)
    x += dx
    fb = f(x)
    return (fb - fa) / dx


def get_2_difference_value(f: types.FunctionType, x: float, dx: float) -> float:
    """

    Example of usage:
    * get_difference_value(math.sin, 1, 0.000001) -> -0.84....

    !Important information:
    The best delta x is 0.000001 for every case
    """

    fa = f(x)
    x += dx
    fb = f(x)
    x += dx
    fc = f(x)
    return (fc - 2 * fb + fa) / (dx * dx)


def quick_sort(src: list[typing.Any]):
    """

    Example of usage:
    *
    """

    less = []
    equal = []
    greater = []
    if len(arr) > 0:
        p = src[0]
        for i in src:
            if i == p:
                equal.append(i)
            elif i > p:
                greater.append(i)
            else:
                less.append(i)
        return quick_sort(less) + equal + quick_sort(greater)
    return arr


def calculate_reversed_polish_notation(src: str) -> float:
    operators = ["+", "-", "*", "/", "^"]
    token_list = src.split(" ")

    operands = []
    for token in token_list:
        if token in operators:
            operand2 = operands.pop()
            operand1 = operands.pop()
            result = 0
            if token == "+":
                result = operand1 + operand2
            elif token == "-":
                result = operand1 - operand2
            elif token == "*":
                result = operand1 * operand2
            elif token == "/":
                result = operand1 / operand2
            elif token == "^":
                result = operand1 ** operand2
            operands.append(result)
            continue
        operands.append(float(token))
    return operands.pop()


def get_sqrt_of_2_by_taylor_series(eps: float = 0.000000000000001) -> float:
    """

    Example of usage:
    *  get_sqrt_of_2_by_taylor_series() -> 1.4142...

    !Important information:
    * This function uses a method of taylor series, which
    * consists of such formula: (f**(n)(Xn) / n!) * (Xn - X0)
    """

    diff = 10000
    n = 1
    s = 1
    c = 1
    while diff > eps:
        c *= ((-2 * n + 3) * 0.999) / (2 * n)
        s += c

        diff_c = c
        if diff_c < 0:
            diff_c *= -1

        diff = diff_c

        n += 1
    return s


def find_first_and_second_max(src: list[float]) -> tuple[float, float]:
    """
    Example of usage:
    * find_first_and_second_max([1, 2, 3, 4]) -> (4, 3)
    * find_first_and_second_max([-8, -3, -2, -10]) -> (-2, -3)
    """

    if len(src) == 0:
        return 0, 0

    max_2 = max_1 = src[0]
    for i in src:
        if i > max_1:
            max_2 = max_1
            max_1 = i
        elif i < max_1 and (i > max_2 or max_1 == max_2):
            max_2 = i
    return max_1, max_2


def ask_user_to_input_numbers() -> list[float]:
    r = []
    while True:
        x = 0
        try:
            x = float(input("Please, pass your number: "))
        except ValueError:
            print("Your value should be of type 'float', try again")
            continue
        r.append(x)

        q = False
        while True:
            w = input("If you want to stop, write 'q'. If you want to continue, write 'c': ")
            if w == "q" or w == "c":
                if w == "q":
                    q = True
                break
            else:
                print("Please, chose correct answer")
                continue
        if q:
            break
    return r


def ddd(x: float, epsilon: float = 0.000001):
    """

    Example of usage:
    * ddd(0.99) -> 1.4142...
    """

    suma = 1
    an = 1
    n = 0
    while True:
        an *= (-x * (2 * n - 1)) / (2 * (n + 1))
        suma += an
        n += 1
        if abs(an) < epsilon:
            return suma


def get_taylor_series_example(n: float, eps: float):
    """

    Example of usage:
    * get_taylor_series_example(10, 0.00001) -> ...
    """

    if n >= 1:
        print("Your 'n' param should be less than 1")
        return 0

    suma = 1
    res = 1
    x = 1
    while abs(res) >= eps:
        if x % 2 == 0:
            res = ((get_factorial(2 * x)) / ((1 - 2 * x) * (get_factorial(x) ** 2) * 4 ** x)) * n ** x
            suma += res
        else:
            res = -((get_factorial(2 * x)) / ((1 - 2 * x) * (get_factorial(x) ** 2) * 4 ** x)) * n ** x
            suma += res
        x += 1

    return suma


def binary_search(src: list[typing.Union[int, float]], x: float) -> int:
    """

    Example of usage:
    * binary_search([1, 2, 3], 10) -> -1
    * binary_search([1, 2, 3], 2) -> 1
    """

    mid = start = 0
    end = len(src) - 1

    while start <= end:
        mid = (start + end) // 2

        if src[mid] < x:
            start = mid + 1
        elif src[mid] > x:
            end = mid - 1
        else:
            return mid

    return -1
