#sphere2.py
#solves for area and volume of a sphere

import math


def sphereArea(radius):
    area = 4 * math.pi * radius**2
    print("The surface area of this sphere is",area,".")




def sphereVolume(radius):
    volume = (4/3) * math.pi * radius**3
    print("The volume of this sphere is",volume,".")


sphereVolume(7), sphereArea(7)
