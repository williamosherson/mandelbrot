import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
def mandelbrot(x, y, threshold):
    """Calculates whether the number c = x + i*y belongs to the 
    Mandelbrot set. In order to belong, the sequence z[i + 1] = z[i]**2 + c
    must not diverge after 'threshold' number of steps. The sequence diverges
    if the absolute value of z[i+1] is greater than 4.
    
    :param float x: the x component of the initial complex number
    :param float y: the y component of the initial complex number
    :param int threshold: the number of iterations to considered it converged
    """
    # initial conditions
    c = complex(x, y)
    z = complex(0, 0)
    
    for i in range(threshold):
        z = z**2 + c
        if abs(z) > 2:  # it diverged
            return i
        
    return threshold - 1  # it didn't diverge
x_start, y_start = -2, -1.5  # an interesting region starts here
x_end,y_end = 2,1.5
x_focus = -0.7797866265
y_focus = -0.1343358625


fig = plt.figure(figsize=(10, 10))  # instantiate a figure to draw
ax = plt.axes()  # create an axes object

def animate(i):
    re = np.linspace(x_start*(1.3**-i)+x_focus, x_end*(1.3**-i)+x_focus, 450)
    im = np.linspace(y_start*(1.3**-i)+y_focus,y_end*(1.3**-i)+y_focus,450)

    ax.clear()  # clear axes object
    ax.set_xticks([], [])  # clear x-axis ticks
    ax.set_yticks([], [])  # clear y-axis ticks
    
    X = np.empty((len(re), len(im)))  # re-initialize the array-like image
    for i in range(len(re)):
        for j in range(len(im)):
            X[i, j] = mandelbrot(re[i], im[j],20)
    
    # associate colors to the iterations with an iterpolation
    img = ax.imshow(X.T, interpolation="bicubic", cmap='twilight_shifted')
    return [img]
 
anim = animation.FuncAnimation(fig, animate, frames=10, interval=100, blit=True)
anim.save('mandelbrot2.gif',writer='pillow')