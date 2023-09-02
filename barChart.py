from matplotlib import pyplot as plt

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

plt.bar(x=movies, height = num_oscars, width=0.5, bottom=0, align='center')

plt.title("My Favorite Movies")
plt.ylabel('# Awards')

plt.xticks(range(len(movies)), movies)
plt.show()
