#https://stackoverflow.com/questions/9489669/updating-a-matplotlib-bar-graph

import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
import numpy as np

values = [0, 10, 20, 30, 40, 50]

def animated_barplot(n):
    # http://www.scipy.org/Cookbook/Matplotlib/Animations
    x = values
    rects = plt.barh(range(N), x, align = 'center')
    for i in range(50):
        x = mu + sigma*np.random.randn(N)
        for rect, h in zip(rects, x):
            rect.set_height(h)
        fig.canvas.draw()

fig = plt.figure()
win = fig.canvas.manager.window
win.after(100, animated_barplot)
plt.show()
