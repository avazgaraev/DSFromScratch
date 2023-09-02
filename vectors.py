from typing import List

Vector = List[float]

def subtract(v: Vector, w: Vector) -> Vector:
    return [v_i - w_i for v_i, w_i in zip(v,w)]
#print(subtract([3,4,5], [2,5,3]))
#%% Sum of vectors
from typing import List

Vector = List[float]

def sumOfVectors(vectors: List[Vector]) -> Vector:
    num_list = len(vectors[0])
    #print(vectors[0])

    return [sum(vector[i] for vector in vectors)
            for i in range(num_list)]
print(sumOfVectors([[1,2,4,5],[4,5,7,5]]))
#%%
from typing import List

def dot(v:Vector, w:Vector) ->float:
    assert len(v) == len(w), "lenght must be the same"
    return sum(v_i* w_i for v_i, w_i in zip(v, w))
dot([3,4,5], [4,5,6])
# %% Magnitude of Vector
from typing import List
import math
def SquareForMagnitude(v: Vector) -> float:
    return sum(v_i**2 for v_i in v)

def magnitude(v: Vector) ->float:
    return math.sqrt(SquareForMagnitude(v))
magnitude([6,8])
# %% Distance between 2 vectors
from typing import List
import math

def subtract(v: Vector, w: Vector) -> Vector:
    return [v_i - w_i for v_i, w_i in zip(v,w)]

def SquareForMagnitude(v: Vector) -> float:
    return sum(v_i**2 for v_i in v)

def magnitude(v: Vector) ->float:
    return math.sqrt(SquareForMagnitude(v))

def distance(v: Vector, w:Vector) -> float:
    return magnitude(subtract(v,w))

distance([3,4,5], [6,8,10])
# %%
