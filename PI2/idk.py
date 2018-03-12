import matplotlib.pyplot as plt
from matplotlib import animation

fig=plt.figure()

n=100 #Number of frames
array = [10,20,30]
x = range(1,4)
barcollection = plt.bar(x, array)

def animate(i):
    y = [m + 1 for m in array]
    for i in range(3):
        array[i] += 1
    for i, b in enumerate(barcollection):
        b.set_height(y[i])

anim=animation.FuncAnimation(fig,animate,repeat=False,blit=False,frames=n,
                             interval=100)


plt.show()
