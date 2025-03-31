from PIL import Image 
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.cm as cm 
height = 1000
width = 1000
image = Image.new('RGB',(width,height))
def set_pixel(image):
    for y in range(height):
        for x in range(width):
            X=x*2.5/width -2
            Y= y*2.8/height -1.4
            z=0
            iteration = 0 
            while np.absolute(z) <2 and iteration <50:
                z=z**2 +X+Y*1j
                iteration += 1
            color_rgb = tuple(int(c * 255) for c in cm.twilight_shifted(iteration / 50)[:3])  # Convert color to RGB values

            image.putpixel((x,y),color_rgb)
    return image 
based = set_pixel(image)
# Save the modified image
output_path = r'C:\Users\vilmo\OneDrive\Pictures\image generator test\mandlebrotito.jpg'
based.save(output_path)



            