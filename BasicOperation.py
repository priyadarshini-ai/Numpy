import numpy as np

arr=np.array([[1,2,3,4],[5,6,7,8]])
print("SUM OF ALL ELEMENTS IN ARRAY IS: ",arr.sum()) # PRINTS THE SUM OF ALL ELEMENTS IN ARRAY

arr1=np.array([[4,3,2,1],[8,7,6,5]])

arr2=arr+1  # ADDING 1 TO ALL THE ELEMENTS IN AN ARRAY
print(arr2)

arr3=arr+arr1 #SUM OF TWO ARRAYS
print(arr3)