import numpy as np

def median_bins(values, B):
  #main variables (returns)
  mean = np.mean(values)
  stdev = np.std(values)
  bin_counts = np.zeros((B,)) # init with zeroes - , dtype=np.int
  n_smaller = 0
  
  #aux variables
  width = 2*stdev / B
  minval = mean-stdev
   
  for value in values: # for all the values in the array
    binmax = minval
    
    if value < minval : #skip this value
      n_smaller += 1
    else: # fit into a bin
      for index in range(B):
        binmax += width
        if value < binmax: #values > maxval -> ignored
          bin_counts[index] += 1
          break
  return (mean, stdev, n_smaller, bin_counts)


def median_approx(values, B):
  median_bins_result = median_bins(values, B)
  
  #resuts of bin calculation
  mean = median_bins_result[0]
  stdev = median_bins_result[1]
  n_smaller = median_bins_result[2]
  bins = median_bins_result[3]
    
  #other aux calculations
  minval = mean - stdev
  target_total = (len(values)+1)/2
  width = 2*stdev / B
  running_total = n_smaller
  
  #print("minval:", minval, "width:", width, ", running_total/n_smaller: ", running_total)
  
  for index in range(len(bins)): #go over every bin
     running_total += bins[index]
     #print("idx: ", index, "rt: ", running_total, ", target_total: ", target_total)
     if running_total >= target_total: 
        return minval + width/2 + index*width
  return minval + width/2 + index*width

# You can use this to test your functions.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your functions with the first example in the question.
  print(median_bins([1, 1, 3, 2, 2, 6], 3))
  print(median_approx([1, 1, 3, 2, 2, 6], 3)) #2.5
  
  # Run your functions with the second example in the question.
  print(median_bins([1, 5, 7, 7, 3, 6, 1, 1], 4))
  print(median_approx([1, 5, 7, 7, 3, 6, 1, 1], 4)) #4.50544503131
  
  #3rd case
  print(median_bins([0, 1], 5))
  print(median_approx([0, 1], 5)) #0.9

  # Pathological case
  print(median_bins([1, 1, 1000], 5))
  print(median_approx([1, 1, 1000], 5)) #-42.7464930162


