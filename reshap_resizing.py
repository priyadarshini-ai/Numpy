import numpy as np
arr=np.array([1,2,3,4,5,6,7,8])

# reshaped = np.reshape(arr, (2, 4))
# print(reshaped)

arr.resize((8,3))
print("resized array: ",arr) #IT ADJUSTS THE ARRAY ACCORDING TO SIZE