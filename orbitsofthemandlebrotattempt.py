import numpy as np 
import matplotlib.pyplot as plt
from PIL import Image
figure = plt.figure(figsize=(10, 10))
ax = plt.axes()
ax.set_xlim(-2,0.5)
ax.set_ylim(-1.4,1.4)
ax.imshow(Image.open("C:/Users/vilmo/OneDrive/Pictures/image generator test/mandlebrotito.jpg"), extent=(-2,0.5,-1.4,1.4))
lines = []
coord = None

def on_mouse_move(event):
    global coord
    if event.inaxes :
        
        x =event.xdata
        y =event.ydata
        C= x+y*1j
        z = 0
        X=[]
        Y=[]
        k=0
        while k<20 and abs(z)<3:
            z = z*z + C
            X.append(np.real(z))
            Y.append(np.imag(z))
            k+=1
        for line in lines:
            line.remove()  # Remove the previous lines
        lines.clear()  # Clear the list of lines
        for i in range(k-1):
            line = ax.plot([X[i], X[i+1]], [Y[i], Y[i+1]],color=plt.cm.rainbow(i/(k-1)),marker = "o",markersize = 3)
            lines.extend(line)  # Add the new lines to the list
        figure.canvas.draw()
        if coord is not None:
            coord.remove()        
        coord = ax.annotate(text=f'({str(x)[:9]}+{str(y)[:9]}i)',xy=(X[0],Y[0]),xytext=(X[0],Y[0]),color = 'yellow', fontsize = 12)
        

figure.canvas.mpl_connect('motion_notify_event', on_mouse_move)

plt.show()