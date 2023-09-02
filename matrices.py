#%%
from typing import List, Tuple
Matrix = List[List[float]]

def shape(v: Matrix) -> Tuple[int, int]:
    num_row = len(v)
    num_col = len(v[0])
    return num_row, num_col
print(shape([[1,2,3],[4,5,6]]))
# (2,3)

#%%
from typing import Callable
from typing import List, Tuple

Matrix = List[List[float]]

def shape(num_row: int, num_col: int, entry_fn: Callable[[int, int], float]) -> Matrix:
    return [[entry_fn(i, j) for j in range(num_col)] for i in range(num_row)]


def identity_matrix(n: int) ->Matrix:
    return shape(n,n, lambda i,j:1 if i==j else 0) 
print(identity_matrix(5))
# %%
from typing import Callable
from typing import List, Tuple

Matrix = List[List[float]]
dist = set()

def shape(num_row: int, num_col: int, entry_fn: Callable[[int, int], float]) -> Matrix:
    return [[entry_fn(i, j) for j in range(num_col)] for i in range(num_row)]

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
(4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]


for i, j in friendships:
    dist.add(i)
    dist.add(j)
friend_matrix: Matrix = shape(len(dist), len(dist), lambda i,j:0)
def friendMatrix() ->Matrix:
    for i,j in friendships:
        friend_matrix[i][j]=1
        friend_matrix[j][i]=1
    return friend_matrix

print(friendMatrix())

# %%