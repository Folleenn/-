import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import mymodule
from mymodule import circle_area
from mymodule import circle_len as perimeter
import mymodule as mm


print("1) mymodule.circle_area(5) =", mymodule.circle_area(5))
print("2) circle_area(5)          =", circle_area(5))
print("3) perimeter(5)            =", perimeter(5))
print("4) mm.PI                   =", mm.PI)

print([
    name
    for name in dir(mymodule)
    if not name.startswith("__")
])

print("mymodule.__file__ =", mymodule.__file__)
print("mm._helper() =", mm._helper())
print("sphere_volume(2) =", mymodule.sphere_volume(2))
print("Документация:")
print(mymodule.sphere_volume.__doc__)