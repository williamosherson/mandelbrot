import numpy as np 
import matplotlib.pyplot as plt 
plt.style.use('dark_background')


def mandelbrot_set(h_range, w_range, max_iterations):
	# top left to bottom right
	y, x = np.ogrid[1.4: -1.4: h_range*1j, -1.8: 1: w_range*1j]
	a_array = x + y*1j
	z_array = np.zeros(a_array.shape)
	iterations_till_divergence = max_iterations + np.zeros(a_array.shape)

	for i in range(max_iterations):
		# mandelbrot equation
		z_array = z_array**2 + a_array

		# make a boolean array for diverging indicies of z_array
		z_size_array = z_array * np.conj(z_array)
		divergent_array = z_size_array > 4

		iterations_till_divergence[divergent_array] = i

		# prevent overflow (numbers -> infinity) for diverging locations
		z_array[divergent_array] = 0 
    
	return iterations_till_divergence

plt.imshow(mandelbrot_set(2000, 2000, 70), cmap='twilight_shifted')
plt.axis('off')
plt.savefig('mandelbrot.png', dpi=300)
plt.close()