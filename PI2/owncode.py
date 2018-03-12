# https://stackoverflow.com/questions/9489669/updating-a-matplotlib-bar-graph
# https://stackoverflow.com/questions/10944621/dynamically-updating-plot-in-matplotlib

import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
import numpy as np

# need to define N
N = 5
x = [10, 20, 30, 50, 60]
rects = plt.bar(range(N), x,  align = 'center')

def update_graph():
    x = [60, 50, 30, 20, 10]
    for rect, h in enumerate(rects):
        # probably going through each bar in the graph
        h.set_height(x[rect])
    fig.canvas.draw()


# creates a new figure
fig = plt.figure()

# idk what any of this is pls help
# need it for updating graphs?
win = fig.canvas.manager.window
plt.show()

win.after(100, update_graph)
plt.show()
