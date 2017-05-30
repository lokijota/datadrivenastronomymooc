# Mean and Median of a 1D array from a file

import numpy as np

def calc_stats(filename):
  data = np.loadtxt(filename, delimiter=',')
  # print(data)
  # print(round(np.mean(data),1))
  # print(round(np.median(data),1))
  return (round(np.mean(data),1), round(np.median(data),1))
  

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your `calc_stats` function with examples:
  mean = calc_stats('data1.csv')
  print(mean)
