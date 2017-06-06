from astropy.io import fits
import numpy as np
import time
import sys

# calculate median using numpy
def median_fits(filenames):
  execution_time = 0.0
  
  start = time.perf_counter() #start counting time
 
  images = [ ]
  
  for fitsfile in filenames:
    hdulist = fits.open(fitsfile)
    images.append(hdulist[0].data)
    #print(hdulist[0].data.shape)
  
  array_of_images = np.array(images) # from here: https://stackoverflow.com/questions/13753251/median-combining-fits-images-in-python
  median_image = np.median(array_of_images, axis=0)
  
  execution_time = time.perf_counter() - start #calculate duration
  memory_usage_kb = sys.getsizeof(array_of_images)/1024
  
  return ( median_image, execution_time, memory_usage_kb )


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with first example in the question.
  result = median_fits(['image0.fits', 'image1.fits'])
  print(result[0][100, 100], result[1], result[2])
  
  # Run your function with second example in the question.
  result = median_fits(['image{}.fits'.format(str(i)) for i in range(11)])
  print(result[0][100, 100], result[1], result[2])
