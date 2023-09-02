from matplotlib import pyplot as plt
mentions = [500, 505]
years = [2017, 2018]

plt.bar(years, mentions, 0.8)

plt.xticks(years)
plt.axis([2016.5, 2018.5, 0, 550])

plt.show()