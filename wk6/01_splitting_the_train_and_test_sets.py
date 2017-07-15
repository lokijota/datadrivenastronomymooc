import numpy as np
import math


def splitdata_train_test(data, fraction_training):
  #randomize data set order
  np.random.seed(0)
  np.random.shuffle(data)

  #find split point
  training_rows = math.floor(len(data) * fraction_training) #int(...) would be enough
  
  training_set = data[0:training_rows] #or data[:training_rows]
  testing_set = data[training_rows:len(data)] #or data[training_rows:]
  return (training_set, testing_set)

if __name__ == "__main__":
  data = np.load('galaxy_catalogue.npy')

  # set the fraction of data which should be in the training set
  fraction_training = 0.7

  # split the data using your function
  training, testing = splitdata_train_test(data, fraction_training)

  # print the key values
  print('Number data galaxies:', len(data))
  print('Train fraction:', fraction_training)
  print('Number of galaxies in training set:', len(training))
  print('Number of galaxies in testing set:', len(testing))

