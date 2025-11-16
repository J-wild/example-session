
# Reading text

# open and read the whole file



f = open("exampletext.txt", "rt")
print(f.read())





#loop through and read line by line
"""
with open("exampletext.txt") as f:
  for x in f:
    print(x) 

"""


#Writing text

"""
with open("exampletext.txt", "a") as f:
  f.write("Now the file has more content!")

#open and read the file after the appending:
with open("exampletext.txt") as f:
  print(f.read()) 

"""


#create a new file

"""
f = open("myfile.txt", "x")
"""

# x - creates a file