# typeOfRect < 0  -->  left rectangle method
# typeOfRect == 0  -->  middle rectangle method
# typeOfRect > 0  -->  right rectangle method
def rect_method(f, l: float, r: float, n: int, typeOfRect: int):
    assert n > 0, "Колличество разбиений не может быть менее 1"
    assert l <= r, "Левая граница должна быть меньше правой"
    ans, dx = 0, (r - l) / n
    l += 0 if typeOfRect < 0 else (dx / 2.0 if typeOfRect == 0 else dx)
    for i in range(n):
        ans += f(l + dx * i)
    return ans * dx


def trapezoid_method(f, l: float, r: float, n: int):
    assert n > 0, "Колличество разбиений не может быть менее 1"
    assert l <= r, "Левая граница должна быть меньше правой"
    ans, dx = (f(l) + f(r)) / 2.0, (r - l) / n
    for i in range(1, n):
        ans += f(l + dx * i)
    return ans * dx


def simpson_method(f, l: float, r: float, n: int):
    assert n > 0, "Колличество разбиений не может быть менее 1"
    assert n % 2 == 0, "Для метода Симпсона необходимо разбивать на четное количество отрезков"
    assert l <= r, "Левая граница должна быть меньше правой"
    ans, dx = f(l) + f(r), (r - l) / n
    for i in range(1, n, 2):
        ans += 4.0 * f(l + i * dx)
    for i in range(2, n - 1, 2):
        ans += 2.0 * f(l + i * dx)
    return ans * dx / 3.0


def call_method_by_id(f, l: float, r: float, n: int, method_id: int):
    if 0 <= method_id <= 2:
        return rect_method(f, l, r, n, int(-1) + method_id)
    elif method_id == 3:
        return trapezoid_method(f, l, r, n)
    return simpson_method(f, l, r, n)


def find_integral_and_n(f, l: float, r: float, precision: float, method_id: int):
    n: int = 4
    while True:
        I0 = call_method_by_id(f, l, r, n, method_id)
        n *= 2
        I1 = call_method_by_id(f, l, r, n, method_id)
        if abs(I1 - I0) < precision:
            return I1, n
