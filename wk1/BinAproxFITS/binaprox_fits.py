from helper import running_stats # Import the running_stats function
from astropy.io import fits
import numpy as np
import time

# Write your median_bins_fits and median_approx_fits here:
def median_bins_fits(filenames, nbins):
  #main variables (returns)
  mean, stdev = running_stats(filenames) #each has 200x200 dimensions
  n_smaller = np.zeros(mean.shape)
  bin_counts = np.zeros((mean.shape[0],mean.shape[1],nbins));
  
  minval = mean-stdev #matrix operation
  width = 2*stdev/nbins
  
  # process every image one at a time
  for fitsfile in filenames:
    hdulist = fits.open(fitsfile)
    image = hdulist[0].data
    
    # for every pixel in the image
    for x in range(0, mean.shape[0]):
      for y in range(0, mean.shape[1]):
        binmax = minval[x,y]
        value = image[x,y]
 
        if value < minval[x,y] : #skip this value
          n_smaller[x,y] += 1
        else: # fit into a bin
          for index in range(nbins):
            binmax += width[x,y]
            if value < binmax: #values > maxval -> ignored
              bin_counts[x,y,index] += 1
              break

  return (mean, stdev, n_smaller, bin_counts)

def median_approx_fits(filenames, nbins):
  mean, stdev, n_smaller, bins = median_bins_fits(filenames, nbins) #resuts of bin calculation
  minval = mean - stdev #matrix operation
  width = 2*stdev/nbins #matrix operation
  
  result = np.zeros(mean.shape)
  
  for x in range(0, result.shape[0]):
      for y in range(0, result.shape[1]):
        running_total = n_smaller[x, y]
        target_total = (len(filenames)+1)/2

        for index in range(nbins):
           running_total += bins[x,y,index]
           if running_total >= target_total:
             result[x,y] = minval[x,y] + width[x,y]/2 + index*width[x,y]
             break

  return result
  
# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with examples from the question.
  seconds = 0.0
  start = time.perf_counter()
  mean, std, left_bin, bins = median_bins_fits(['image0.fits', 'image1.fits', 'image2.fits'], 5)
  print("duration median_bins_fits",  time.perf_counter() - start)
  
  start = time.perf_counter()
  median = median_approx_fits(['image0.fits', 'image1.fits', 'image2.fits'], 5)
  print("duration median_approx_fits",  time.perf_counter() - start)

