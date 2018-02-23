# update the data of the plot objects

"""x = np.linspace(0, 6*np.pi, 100)
y = np.sin(x)
fig = plt.figure()
ax = fig.add_subplot(111)
line1, = ax.plot(x, y, 'r-') # Returns a tuple of line objects, thus the comma
for phase in np.linspace(0, 10*np.pi, 500):
    line1.set_ydata(np.sin(x + phase))
    fig.canvas.draw()
    set_ydata
"""

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot

objects = ('1', '2', '3')
y_pos = np.arange(len(objects))
occupancy = [85,80,60]
 
plt.barh(y_pos, occupancy, align='center', alpha=.5)
plt.yticks(y_pos, objects)
plt.xticks(np.arange(0, 100, 25))
plt.xlim(0, 100)
plt.xlabel('Occupancy')
plt.ylabel('Car Number')
plt.title('Train Occupancy')

# (graphname?).set_ydata(numpy.append(hl.get_xdata(), new_data))

plt.show()
