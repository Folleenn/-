import sys
import math
import random

print("Версия Python:", sys.version.split()[0])
print("Интерпретатор:", sys.executable)

print("Количество путей:", len(sys.path))
for path in sys.path[:5]:
    print("   ", path)

print("math.pi =", math.pi)
print("random.random() =", random.random())

print("Всего загружено модулей:", len(sys.modules))
print("Первые: ", sorted(sys.modules)[:5])

public_math = [
    name for name in dir(math)
    if not name.startswith("_")
]

print("Публичных имён: ", len(public_math))
print("Первые: ", public_math[:8])

print("Имя текущего модуля:", __name__)