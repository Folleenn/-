import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import geometry

from geometry.flat import (
    triangle_area,
    circle_area
)
from geometry.solid import hemisphere_area
from geometry.solid import sphere_volume


print("Версия geometry:", geometry.__version__)

print("circle_area(3) =", round(circle_area(3), 4))
print("triangle_area(6, 4) =", triangle_area(6, 4))
print("sphere_volume(3) =", round(sphere_volume(3), 4))
print("hemisphere_area(3) =", round(hemisphere_area(3), 4))
print("geometry.__all__ =", geometry.__all__)
print("geometry.__file__ =", geometry.__file__)