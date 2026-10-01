import random
from collections import Counter

random.seed(42)

print("random()             :", f"{random.random():.6f}")
print("uniform(1, 10)       :", f"{random.uniform(1, 10):.3f}")
print("randint(1, 6)        :", random.randint(1, 6))
print("randrange(0,100,5)   :", random.randrange(0, 100, 5))

print("\n--- Бросок двух кубиков, 5 раз ---")

for i in range(1, 6):
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    print(f"Бросок {i}: {a} + {b} = {a + b}")

counts = Counter(
    random.randint(1, 6)
    for _ in range(10_000)
)

print("\n--- Статистика 10000 бросков одного кубика ---")

for face in range(1, 7):
    cnt = counts[face]
    percent = cnt / 10_000 * 100

    print(
        f"{face}: {cnt:5d} "
        f"({percent:5.2f}%)"
    )

    print(
        f"   отклонение от 16.67%: "
        f"{percent - 16.67:+.2f} п.п."
    )

triple = Counter(
    sum(random.randint(1, 6) for _ in range(3))
    for _ in range(100000)
)

most_common = triple.most_common()

print("\n--- Доп. задание: 3 кубика, 100000 бросков ---")
print(
    "Самая частая сумма:",
    most_common[0][0],
    most_common[0][1],
    "раз"
)