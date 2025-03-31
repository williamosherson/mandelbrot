import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

fig = plt.figure(figsize=(10, 10))  # instantiate a figure to draw
ax = plt.axes()

def mandelbrot_set(h_range,w_range,itmax):
    y,x = np.ogrid[-1.4:1.4:h_range*1j,-2:0.5:w_range*1j] #create complex grid 
    c_array = x+y*1j                                      #array containing all values of the mandelbrotset 
    z_array=np.zeros(c_array.shape)                       #an array of z same shape as c set to all 0
    diverged_at_iteration = itmax+np.zeros(c_array.shape)  #will be transformed into mandelbrott image, set all values iniitally to 32 because values that do not diverege should have the max iteration value

    not_yet_diverged = c_array<1000                        #array of same shape as c with all values set to True 
    for i in range(itmax):                                 #loops for all iterations
        z_array=z_array**2+c_array                         #calculates the values of the points in array after i itterations 

        z_size_array = z_array*np.conj(z_array)                        #creates an array of the magnitude of the values of z_array 
        divergent_array = z_size_array>4                   #checks which values of z_size's magnitudes indicate divergence 
        diverging_now = divergent_array & not_yet_diverged #creates a boolean matrix whos values are true if the value in the same spot in z_size's value just surpassed 2 this iteration
        diverged_at_iteration[diverging_now]=i              #stores the iterations needed for the values of the z_array to diverge, which have divereged in this iteration 

        z_array[divergent_array] = 0 #prevent overflow, if value has diverged it can be set to zero as it will never be on in diverging_now again
    return(diverged_at_iteration)

anim=animation.FuncAnimation(fig,)
plt.axis()
plt.show()