import numpy as np
arr = np.array([[4, 3, 2, 1], [3, 4 ,5 ,6]])
print(arr[1,3])
# [1,3] 1 = baris, 3 = kolom
arr[1][3]=14
print(arr[1,3])

print("--------------")

for x in arr:
    for y in x:
        print(y)