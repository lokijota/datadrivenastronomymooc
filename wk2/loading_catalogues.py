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
    result.append((count, hms2dec(line[0], line[1], line[2]), dms2dec(line[3], line[4], line[5])))
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

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Output of the import_bss and import_super functions
  bss_cat = import_bss()
  super_cat = import_super()
  print(bss_cat)
  print(super_cat)
