import numpy as np
arr=np.array([4,5.1,6,7.4])
arr1=np.array([[1,2,3,4],[2,3,4,5]])

print(arr.sum(dtype=int))
print(arr.sum(dtype=float))
print("Sum of arr : ", np.sum(arr).dtype == np.float64) #true
print("Sum of arr : ", np.sum(arr).dtype == np.int64)

print(np.mean(arr)) # Mean of the array elements
print(np.mean(arr1,axis=1))
print(np.mean(arr1,axis=0))


