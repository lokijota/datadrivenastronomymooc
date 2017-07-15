import numpy as np

# same as:
# SELECT kepler_id, radius
# FROM Star
# WHERE radius > 1.0;

def query(csv_filename):
  data = np.loadtxt(csv_filename, delimiter=',', usecols=(0,2))
  output = []
  
  for star in data:
    if star[1] > 1.0:
      output.append(star)
  
  return np.array(output)

# You can use this to test your code
# Everything inside this if-statement will be ignored by the automarker
if __name__ == '__main__':
  # Compare your function output to the SQL query
  result = query('stars.csv')
  print (result)
