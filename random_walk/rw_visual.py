import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    # Make a random walk
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # plot the points in the walk
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
    num_points = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=num_points, 
               cmap=plt.cm.Blues, edgecolor='none', s=1)
    
    # emphasize the first and last points
    ax.scatter(0, 0, c='green', edgecolors='none', s=50)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', 
               edgecolors='none', s=50)

    # remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Do you want to continue? (y/n): ")
    if keep_running.lower() == 'n':
        break