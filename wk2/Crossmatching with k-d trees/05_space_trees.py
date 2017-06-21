import numpy as np
import statistics
import time
from astropy.coordinates import SkyCoord
from astropy import units as u

def crossmatch(cat1, cat2, max_dist):
  matches = []
  nomatches = []


  start = time.perf_counter()

  skycat1 = SkyCoord(cat1*u.degree, frame='icrs')
  skycat2 = SkyCoord(cat2*u.degree, frame='icrs')
  closest_ids, closest_dists, closest_dists3d = skycat1.match_to_catalog_sky(skycat2)
  closest_dists_deg = closest_dists.value
  
  for cat1idx in range(len(cat1)):
    if closest_dists_deg[cat1idx] > max_dist:
      nomatches.append(cat1idx)
    else:
      matches.append((cat1idx,closest_ids[cat1idx],closest_dists_deg[cat1idx]))
    
  #closest_dist.value returns an array of degrees
  #print("vals", closest_ids)
  #print("dists", closest_dists)
  #print("dists.val", closest_dists.value)
  
  return (matches, nomatches, time.perf_counter() - start)

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # The example in the question
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

