import math

PI = math.pi
VERSION = "1.0.0"

_secret = PI / 2


def circle_area(r):
    return PI * r ** 2


def circle_len(r):
    return 2 * PI * r


def _helper():
    return _secret

def sphere_volume(r):
    return 4 / 3 * PI * r ** 3


if __name__ == "__main__":
    print("[1.0.0] Самопроверка mymodule:")
    print("S(r=2) =", circle_area(2))
    print("L(r=2) =", circle_len(2))
    print("V(r=2) =", sphere_volume(2))