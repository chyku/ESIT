# update the data of the plot objects

import matplotlib.pyplot as plt
from matplotlib import animation

fig=plt.figure()

n=100 #Number of frames
array = [50,20,10]
x = range(1,4)
barcollection = plt.barh(x, array)

# just graph setup
plt.xlim(0, 100)
plt.xlabel('Occupancy')
plt.ylabel('Car Number')
plt.title('Train Occupancy')
plt.yticks([1, 2, 3])

def animate(i):
    y = [m + m for m in array]
    for i in range(3):
        array[i] += 1
    for i, b in enumerate(barcollection):
        b.set_width(y[i])

# https://matplotlib.org/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation
anim=animation.FuncAnimation(fig,animate,repeat=False,blit=False,frames=n)

plt.show()