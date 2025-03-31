import numpy as np
from PIL import Image
# Create a blank image
width, height =100, 100
realwidth = 2
realheight = 2 
image = Image.new("RGB", (width, height))
def div_checker(C):
    z=0
    try:
        for i in range(15):
            z = z**2+C
            i+=1
    except:
        red = 0
        green = 0
        blue = 0
    else:
        if np.abs(z) > 2:
            red = 0 
            green = 0 
            blue = 0 
        else:
            red=255
            green=255
            blue=255
    return red, green, blue
def set_unique_pixels(image,realwidth,realheight):
    width, height = image.size

    # Iterate over each pixel
    for y in range(height):
        for x in range(width):
            # Map the unique value to RGB components
            C=(x*realwidth/width)-1.5+((y*realheight/height)-1)*1j
            red,green,blue = div_checker(C)
                

            # Set the pixel color to the calculated RGB values
            image.putpixel((x, y), (red, green, blue))

    return image
based = set_unique_pixels(image,realwidth,realheight)
# Save the modified image
output_path = r'C:\Users\vilmo\OneDrive\Pictures\image generator test\colored.jpg'
based.save(output_path)
