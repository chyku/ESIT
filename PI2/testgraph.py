# https://stackoverflow.com/questions/9489669/updating-a-matplotlib-bar-graph
# https://stackoverflow.com/questions/10944621/dynamically-updating-plot-in-matplotlib

import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
import numpy as np

# need to define N
rects = plt.bar(range(N), x,  align = 'center')

def update_graph(data):
    # x = mu + sigma*np.random.randn(N)
    # x is random data values in an array
    for rect, h in zip(rects, data):
        # probably going through each bar in the graph
        rect.set_height(h)
    fig.canvas.draw()

def animated_barplot():
    # http://www.scipy.org/Cookbook/Matplotlib/Animations
    mu, sigma = 100, 15
    N = 4

    # returns random array of 4 values?
    x = mu + sigma*np.random.randn(N)

    # range returns [0 1 2 ... N]
    rects = plt.bar(range(N), x,  align = 'center')
    
    # why range of 50? i isn't even used in this loop
    for i in range(50):
        x = mu + sigma*np.random.randn(N)
        for rect, h in zip(rects, x):
            # returns tuple arrays, no sure what that does lmao
            rect.set_height(h)
        fig.canvas.draw()

# creates a new figure
fig = plt.figure()

# idk what any of this is pls help
# need it for updating graphs?
win = fig.canvas.manager.window
win.after(100, animated_barplot)
plt.show()