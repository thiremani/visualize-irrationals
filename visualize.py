import matplotlib.animation as animation  
import matplotlib.pyplot as plt  
import numpy as np
import math


# creating a blank window
# for the animation
fig = plt.figure()
axis = plt.axes(xlim =(-2, 2),
                ylim =(-2, 2))
  
line, = axis.plot([], [], lw = 1)
   
# what will our line dataset
# contain?
def init():
    line.set_data([], [])
    return line,

# initializing empty values
# for x and y co-ordinates
xdata, ydata = [], []

num = math.e
# animation function
def animate(i):  
    # pt is the complex number determined
    # by the frame number
    theta = i / 20
    a = 1j ** (theta * 2 / math.pi)
    b = 1j ** (num * theta * 2 / math.pi)
    pt = a + b

    # x, y values to be plotted
    x = pt.real
    y = pt.imag

    # appending values to the previously
    # empty x and y data holders
    xdata.append(x)
    ydata.append(y)
    line.set_data(xdata, ydata)

    return line,

# calling the animation function
anim = animation.FuncAnimation(fig, animate, init_func = init,
                               frames = 10000, interval = 10, blit = True)

animwriter = animation.FFMpegWriter(fps=30)
# saves the animation in our desktop
anim.save('irrational.mp4', writer = animwriter)