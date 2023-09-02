from matplotlib import pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000]
gdp = [300.2, 400.2, 500, 600.5, 550.3, 621.4]

plt.plot(years, gdp, color = 'red', marker = 'o', linestyle = 'solid')

plt.title('Nominal GDP')
plt.ylabel('Billions of $')
plt.show()