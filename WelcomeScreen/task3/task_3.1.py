import math

print("=== Константы ===")
print(f"math.pi = {math.pi}")
print(f"math.e = {math.e}")
print(f"math.tau = {math.tau}")
print(
    f"math.inf = {math.inf}, "
    f"-math.inf = {-math.inf}, "
    f"math.nan = {math.nan}"
)

print("\n=== Округления ===")

x = 7.6

print("math.floor(x) =", math.floor(x))
print("math.ceil(x) =", math.ceil(x))
print("round(x) =", round(x))
print("math.trunc(x) =", math.trunc(x))

print("round(2.5) =", round(2.5))
print("round(3.5) =", round(3.5))

print("\n=== Степени, корни, логарифмы ===")

print("math.sqrt(144) =", math.sqrt(144))
print("math.pow(2, 10) =", math.pow(2, 10))
print("2 ** 10 =", 2 ** 10)

print("math.exp(1) =", math.exp(1))
print("math.log(math.e) =", math.log(math.e))
print("math.log(1024, 2) =", math.log(1024, 2))
print("math.log10(1000) =", math.log10(1000))
print("math.log2(1024) =", math.log2(1024))

print("\n=== Факториал, НОД, НОК, комбинаторика ===")

print("math.factorial(10) =", math.factorial(10))
print("math.gcd(48, 180) =", math.gcd(48, 180))
print("math.lcm(4, 6) =", math.lcm(4, 6))
print("math.comb(10, 3) =", math.comb(10, 3))
print("math.perm(10, 3) =", math.perm(10, 3))
print("math.prod([1, 2, 3, 4]) =", math.prod([1, 2, 3, 4]))
print("math.isqrt(50) =", math.isqrt(50))

print("\n=== Точность вещественных чисел ===")

print(
    "0.1 + 0.2 == 0.3:",
    0.1 + 0.2 == 0.3
)

print(
    "math.isclose(0.1 + 0.2, 0.3):",
    math.isclose(0.1 + 0.2, 0.3)
)

print(
    "math.fsum([0.1] * 10):",
    math.fsum([0.1] * 10)
)

print(
    "sum([0.1] * 10):",
    sum([0.1] * 10)
)

print(
    "math.copysign(5, -1):",
    math.copysign(5, -1)
)

print("\n=== comb vs perm ===")

print(
    "Выбрать 3 дежурных из 12:",
    math.comb(12, 3)
)

print(
    "Расставить 3 дежурных по позициям:",
    math.perm(12, 3)
)

f170 = math.factorial(170)
f171 = math.factorial(171)

print(
    "factorial(170), цифр:",
    len(str(f170))
)

print(
    "factorial(171), цифр:",
    len(str(f171))
)

try:
    print(float(f170))
    print(float(f171))
except OverflowError as exc:
    print(
        "OverflowError:",
        exc
    )