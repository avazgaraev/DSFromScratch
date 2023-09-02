from vectors import SquareForMagnitude
from typing import List
import math

grades = [83, 95, 91, 87, 83, 67, 67, 67, 73, 77,77,77,77, 70, 0, 85, 82, 100, 67,67, 73, 77, 0]

def mean(xs:List[float]) ->float:
    return sum(xs)/len(xs)

#Squared and Standard Deviation

def de_mean(xs: List[float])-> List[float]:
    x_bar = mean(xs)
    return [x - x_bar for x in xs]

def variance(xs:List[float]) -> float:
    n=len(xs)
    deviation = de_mean(xs)
    return SquareForMagnitude(deviation)/(n-1)

def standard_dev(xs: List[float]) -> float:
    return math.sqrt(variance(xs))

print(standard_dev(grades))