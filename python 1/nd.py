import numpy as np
arr = np.array([
                [[1, 2, 3], 
                 [4, 5, 6]
                ],
                 
                [[7, 8, 9], 
                 [10, 11, 12]
                ]
                ])
print(arr)

print("--------------------")

print(arr[1,1,2])



print("--------------------")

for x in arr:
    for y in x:
        for z in y:
            print(z)