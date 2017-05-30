# Write your load_fits function here.
# Note: I have no access to the .fits files

from astropy.io import fits
import numpy as np

def load_fits(fitsfile):
  hdulist = fits.open(fitsfile)
  data = hdulist[0].data
  indexOfMax = np.argmax(data) #find absolute index of maximum value
  shapeNumColumns = data.shape[1] #equal to len(data[0,:])
  
  #calculate row and column
  row = int(indexOfMax/len(data[0,:]))
  column = indexOfMax - row* len(data[0,:])
  return (row, column)

if __name__ == '__main__':
  # Run your `load_fits` function with examples:
  bright = load_fits('image2.fits')
  print(bright)

  # You can also confirm your result visually:
  from astropy.io import fits
  import matplotlib.pyplot as plt

  hdulist = fits.open('image1.fits')
  data = hdulist[0].data
  # Plot the 2D image data
  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.show()

 

