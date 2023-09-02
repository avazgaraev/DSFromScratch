#%% Mean
from typing import List

def mean(xs:List[float]) ->float:
    return sum(xs)/len(xs)


#%% Median 
from typing import List

def _median_odd(xs: List[float]) -> float:
    sortedXs = sorted(xs)
    return sortedXs[len(xs) //2]

def _median_even(xs:List[float]) -> float:
    sortedXs: List[float] = sorted(xs)
    return ((sorted(xs)[int(len(sortedXs) / 2 - 1)] + sorted(xs)[int(len(sortedXs) / 2)])/2)
def median(v:List[float]):
    return _median_even(v) if len(v) %2 ==0 else _median_odd(v)

print(median([3,6,8,9,10,12]))
#%% Mode
from typing import List
from collections import Counter
grades = [83, 95, 91, 87, 83, 67, 67, 67, 73, 77,77,77,77, 70, 0, 85, 82, 100, 67,67, 73, 77, 0]

def mode(xs:List[float]) -> List[float]:
    counts = Counter(xs)
    max_num= max(counts.values())
    return [num for num,count in counts.items() if count==max_num]
print(mode(grades))
# %%
