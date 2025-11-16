import numpy as np

arr_1d = np.array([1, 2, 3, 4, 5])

arr_2d = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print(f"2d array:\n {arr_2d}")
print(f"\nTransposed 2d array = \n{arr_2d.T}\n")




#itterating through an array 
arr_2d = np.array([[1,2,3,4,5], [6,7,8,9,10]])
for idx, x in np.ndenumerate(arr_2d):
  print(idx, x)


# searching an array
searchable_array = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(searchable_array == 4)
print(f"\nthe number is located at locations {x}")