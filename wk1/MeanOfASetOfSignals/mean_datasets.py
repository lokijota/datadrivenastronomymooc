# Write your mean_datasets function here
import numpy as np

def mean_datasets(filelist):
  count = 0
  for file in filelist:
    newdata = np.loadtxt(file, delimiter=',')
    if count == 0:
      data = newdata
    else:
     data = data + newdata #adds matrixes
    count = count + 1
 
  data = data/count #calculate the average for each value
  data = np.round(data,1) #round
  
  return data
  

if __name__ == '__main__':
  # Run your function with examples from the question:
  
  print(mean_datasets(['data1.csv', 'data2.csv', 'data3.csv']))
