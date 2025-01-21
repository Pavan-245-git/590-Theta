import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr)
print(arr[1, 1, 2])
#arr[0,2,2]
#arr[1,2,1]

import numpy as pd
arr = arr = np.array([[[1, 1, 2, 3], [4, 4, 5, 6]], [[7, 8, 9, 9], [10, 11, 12, 13]]])
print(arr)
a= int(input("Enter number of rows: "))
b= int(input("Enter the elements: "))
print(arr[a,b])