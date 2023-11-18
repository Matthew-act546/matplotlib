import matplotlib.pyplot as plt

x_value = range(1, 6)
y_value = [x**3 for x in x_value]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Blues, s=40)
# ax.plot(x_value, y_value, linewidth=)

# set chart titles and label axes
ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

ax.axis([0.5, 6, 0.5, 150])

# set size thick label
# ax.tick_params(axis="both", which='major', labelsize=14)
plt.show()
# plt.savefig('tryItMySelf/cubes_plot.png', bbox_inches='tight')
