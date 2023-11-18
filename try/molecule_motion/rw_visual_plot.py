import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    # Make a random walk
    rw = RandomWalk()
    rw.fill_walk()

    # plot the points in the walk
    plt.style.use('classic')
    fig, ax = plt.subplots()
    num_points = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, c='blue') 
    
    # emphasize the first and last points
    # ax.scatter(0, 0, c='green', edgecolors='none', s=1000)
    # ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', 
    #            edgecolors='none', s=1000)

    # remove the axes.
    # ax.get_xaxis().set_visible(False)
    # ax.get_yaxis().set_visible(False)

    plt.show()


    keep_running = input("Do you want to continue? (y/n): ")
    if keep_running.lower() == 'n':
        break