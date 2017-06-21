import numpy as np
import statistics
import time

def hms2dec(h, m, s):
  return 15*(h + m/60 + s/3600)

def dms2dec(d, m, s):
  if (d >= 0):
    return d + m/60 + s/3600
  else:
    return d - m/60 - s/3600

def angular_dist(a1, d1, a2, d2):
  p1 = np.square(np.sin(np.absolute(d1-d2)/2))
  p2 = np.cos(d1)*np.cos(d2)*np.square(np.sin(np.absolute(a1-a2)/2))
  return 2*np.arcsin(np.sqrt(p1+p2))

def crossmatch(cat1, cat2, max_dist):
  matches, nomatches = [], []
  cat1id, cat2id = 0, 0

  start = time.perf_counter()

  # convert everything to radians
  cat1 = np.radians(cat1)
  cat2 = np.radians(cat2)
  max_dist = np.radians(max_dist)
  
  ra2s = cat2[:,0]
  dec2s = cat2[:,1]
  
  for cat1line in cat1:
    dists = angular_dist(cat1line[0], cat1line[1], ra2s, dec2s) 
    min_dist = np.min(dists)
    if(min_dist <= max_dist):
      matches.append((cat1id,np.argmin(dists),min_dist))
    else:
      nomatches.append(cat1id)
    
    cat1id += 1
    
  return (matches, nomatches, time.perf_counter() - start)

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # The example in the question
  ra1, dec1 = np.radians([180, 30])
  cat2 = [[180, 32], [55, 10], [302, -44]]
  cat2 = np.radians(cat2)
  ra2s, dec2s = cat2[:,0], cat2[:,1]
  dists = angular_dist(ra1, dec1, ra2s, dec2s)
  print(np.degrees(dists))

  cat1 = np.array([[180, 30], [45, 10], [300, -45]])
  cat2 = np.array([[180, 32], [55, 10], [302, -44]])
  matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
  print('matches:', matches)
  print('unmatched:', no_matches)
  print('time taken:', time_taken)

  # A function to create a random catalogue of size n
  def create_cat(n):
    ras = np.random.uniform(0, 360, size=(n, 1))
    decs = np.random.uniform(-90, 90, size=(n, 1))
    return np.hstack((ras, decs))

  # Test your function on random inputs
  np.random.seed(0)
  cat1 = create_cat(10)
  cat2 = create_cat(20)
  matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
  print('matches:', matches)
  print('unmatched:', no_matches)
  print('time taken:', time_taken)
