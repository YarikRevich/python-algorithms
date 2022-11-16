import types
import typing
from functools import cache


@cache
def get_factorial(n: int) -> int:
    return 1 if n == 0 else n * get_factorial_n(n - 1)


def get_fibonacci(n: int) -> float:
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
    w = 1
    while n != 0:
        if n % 2 == 1:
            w *= a
        a = a * a
        n //= 2
    return w


def secant_method(f: types.FunctionType, start: int, end: int, eps: int) -> float:
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
    s = 0

    h = (end - start) / n

    prev_fb = None
    prev_ffb = None

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


def get_difference_value(f: types.FunctionType, x: float, dx: float) -> float:
    fa = f(x)
    x += dx
    fb = f(x)
    return (fb - fa) / dx


def quick_sort(src: list[typing.Any]):
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
