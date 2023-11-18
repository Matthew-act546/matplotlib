import matplotlib.pyplot as plt

x_value = range(1, 1001)
y_value = [x**2 for x in x_value]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Blues, s=10)
# ax.plot(x_value, y_value, linewidth=)

# set chart titles and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.axis([0, 1100, 0, 1100000])

# set size thick label
# ax.tick_params(axis="both", which='major', labelsize=14)
plt.show()
#plt.savefig('squares_plot.png', bbox_inches='tight')
