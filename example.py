import numpy as np

arr=np.array([[1,2,3],[4,5,6]]) # 2D ARRAY
print(arr)

arr1=np.array(arr[:2,::2]) #SLICING ARRAY FOR ACCESSING THE ARRAY
print(arr1)


arr2=np.array([[1,3,-4,2],
      [2,3,4,5],
      [6,-1,2,3],
      [2,3,4,8]])

arr3=arr2[[1,3,2,0],[2,3,1,0]]  #*** ACCESSING THE ARRAY ELEMENTS AT SPECIFIC INDICES ***
print(arr3)