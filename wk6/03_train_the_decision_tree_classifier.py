import numpy as np
import math
from sklearn.tree import DecisionTreeClassifier


def splitdata_train_test(data, fraction_training):
  #randomize data set order
  np.random.seed(0)
  np.random.shuffle(data)

  #find split point
  training_rows = math.floor(len(data) * fraction_training)

  #split the data
  training_set = data[0:training_rows]
  testing_set = data[training_rows:len(data)]
  return (training_set, testing_set)

def generate_features_targets(data):
  targets = data['class']

  features = np.empty(shape=(len(data), 13))
  features[:, 0] = data['u-g']
  features[:, 1] = data['g-r']
  features[:, 2] = data['r-i']
  features[:, 3] = data['i-z']
  features[:, 4] = data['ecc']
  features[:, 5] = data['m4_u']
  features[:, 6] = data['m4_g']
  features[:, 7] = data['m4_r']
  features[:, 8] = data['m4_i']
  features[:, 9] = data['m4_z']

  # fill the remaining 3 columns with concentrations in the u, r and z filters
  # concentration in u filter
  features[:, 10] = data['petroR50_u']/data['petroR90_u']
  # concentration in r filter
  features[:, 11] = data['petroR50_r']/data['petroR90_r']
  # concentration in z filter
  features[:, 12] = data['petroR50_z']/data['petroR90_z']

  return features, targets

# complete this function by splitting the data set and training a decision tree classifier
def dtc_predict_actual(data):
  # split the data into training and testing sets using a training fraction of 0.7
  training_set, testing_set = splitdata_train_test(data, 0.7)
  
  # generate the feature and targets for the training and test sets
  # i.e. train_features, train_targets, test_features, test_targets
  features_training, targets_training = generate_features_targets(training_set)
  features_testing, targets_testing = generate_features_targets(testing_set)
  
  # instantiate a decision tree classifier
  dtc = DecisionTreeClassifier()

  # train the classifier with the train_features and train_targets
  dtc.fit(features_training, targets_training)
  
  # get predictions for the test_features
  predictions = dtc.predict(features_testing)

  # return the predictions and the test_targets
  return predictions, targets_testing


if __name__ == '__main__':
  data = np.load('galaxy_catalogue.npy')
    
  predicted_class, actual_class = dtc_predict_actual(data)

  # Print some of the initial results
  print("Some initial results...\n   predicted,  actual")
  for i in range(10):
    print("{}. {}, {}".format(i, predicted_class[i], actual_class[i]))
 

