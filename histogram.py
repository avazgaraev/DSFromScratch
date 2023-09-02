from matplotlib import pyplot as plt
from collections import Counter

grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
histogram = Counter(min(grade // 10 *10 , 90) for grade in grades)

plt.bar(x= [key  for key in histogram.keys()], height = histogram.values(), width = 10, edgecolor = (0,0,0))

plt.xticks([x*10 for x in range(11)])

plt.axis([0, 100, 0, 5])
plt.show()