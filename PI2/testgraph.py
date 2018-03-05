#https://stackoverflow.com/questions/9489669/updating-a-matplotlib-bar-graph

import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
import numpy as np

def animated_barplot():
    # http://www.scipy.org/Cookbook/Matplotlib/Animations
    mu, sigma = 100, 15
    N = 4

    # returns random array
    x = mu + sigma*np.random.randn(N)

    # range returns [0 1 2 ... N]
    rects = plt.bar(range(N), x,  align = 'center')
    for i in range(50):
        x = mu + sigma*np.random.randn(N)
        for rect, h in zip(rects, x):
            # returns tuple arrays, no sure what that does lmao
            rect.set_height(h)
        fig.canvas.draw()

fig = plt.figure()
win = fig.canvas.manager.window
win.after(100, animated_barplot)
plt.show()
