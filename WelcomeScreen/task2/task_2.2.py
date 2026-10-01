import random
import math

suits = "♠♥♦♣"
ranks = "6789TJQKA"

deck = [
    rank + suit
    for suit in suits
    for rank in ranks
]

print("Всего карт в колоде:", len(deck))
print(
    "Рука игрока (sample):",
    random.sample(deck, 5)
)

print(
    "Карта дня (choice):",
    random.choice(deck)
)

print(
    "Лут (choices, 5 шт.):",
    random.choices(
        ["обычная", "редкая", "легендарная"],
        weights=[70, 25, 5],
        k=5
    )
)

shuffled = deck.copy()

random.shuffle(shuffled)

print(
    "После shuffle:",
    shuffled[:6],
    "..."
)

hand_cards = random.sample(deck, 15)

print("\n--- Раздача 3 игрокам по 5 карт ---")

for name, start in zip(
    ("Алиса", "Борис", "Вера"),
    range(0, 15, 5)
):
    print(
        f"{name}:",
        hand_cards[start:start + 5]
    )

lottery = sorted(
    random.sample(range(1, 46), 6)
)

total = math.comb(45, 6)

print("\n--- Доп. задание: лотерея 6 из 45 ---")
print("Номера:", lottery)
print("Всего комбинаций:", total)
print(
    "Вероятность угадать все:",
    f"1/{total} = {1 / total:.12%}"
)