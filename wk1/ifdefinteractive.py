def add(a, b):
  return a + b

# When your file is the main program (e.g. pressing Run), Python sets __name__ to __main__ and the code inside the if statement runs. 
# When we import your file for testing, __name__ is the module name, so the condition is False and no output is printed. 
# This is a common trick for testing individual files in large programs. 
  
if __name__ == '__main__':
  print(add(2, 3))
  print(add(1, 5))
