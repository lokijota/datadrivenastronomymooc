import numpy as np

def hms2dec(h, m, s):
  return 15*(h + m/60 + s/3600)

def dms2dec(d, m, s):
  if (d >= 0):
    return d + m/60 + s/3600
  else:
    return d - m/60 - s/3600 

def import_bss():
  file = 'bss.dat'
  lines = np.loadtxt(file, usecols=range(1, 7))
  
  count=1
  result = [ ]
  for line in lines:
    result.append((count, hms2dec(line[0], line[1], line[2]), dms2dec(line[3], line[4]
, line[5])))
    count += 1
  return result

def import_super():
  file = 'super.csv'
  lines = np.loadtxt(file, delimiter=',', skiprows=1,usecols=[0,1])
  result = []
  count = 1
  for line in lines:
    result.append((count, line[0], line[1]))
    count += 1
  return result

def angular_dist(a1, d1, a2, d2):
  a1 = np.radians(a1)
  d1 = np.radians(d1)
  a2 = np.radians(a2)
  d2 = np.radians(d2)

  p1 = np.sin(abs(d1-d2)/2)**2
  p2 = np.cos(d1)*np.cos(d2)*np.sin(abs(a1-a2)/2)**2
  p3 = 2*np.arcsin(np.sqrt(p1+p2))
  return np.degrees(p3)

def crossmatch(cat1, cat2, max_dist):
  matches = []
  nomatches = []
  
  for cat1line in cat1:
    found = False
    best_match = (0,0,max_dist+1)
    
    for cat2line in cat2:
      dist = angular_dist(cat1line[1], cat1line[2], cat2line[1], cat2line[2])
      if(dist <= best_match[2]):
        best_match = (cat1line[0], cat2line[0], dist)
    
    if(best_match[2] <= max_dist):
      matches.append( best_match )
    else:
      nomatches.append( cat1line[0] )
  
  return (matches, nomatches)

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  bss_cat = import_bss()
  super_cat = import_super()

  # First example in the question
  max_dist = 40/3600
  matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
  
  print(matches[:3])
  print(no_matches[:3])

  # Second example in the question
  max_dist = 5/3600
  matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
  print(matches)
  print(matches[:3])
  print(no_matches[:3])
  print(len(no_matches))

