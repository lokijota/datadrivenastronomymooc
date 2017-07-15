import numpy as np

def query(csv_filename):
  data = np.loadtxt(csv_filename, delimiter=',', usecols=(0,2))
  output = []
  
  for star in data:
    if star[1] > 1.0:
      output.append(star)

  unsorted = np.array(output) 
  sorted_indexes = np.argsort(unsorted[:,1])
  return unsorted[sorted_indexes,:]


# You can use this to test your code
# Everything inside this if-statement will be ignored by the automarker
if __name__ == '__main__':
  # Compare your function output to the SQL query
  result = query('stars.csv')
  print (result)
  

