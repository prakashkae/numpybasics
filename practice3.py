import numpy as np


# filtering in numpy

ages = np.array([[21, 17, 19, 20, 16, 30, 18, 65],
                [39, 22, 15, 99, 18, 19, 20, 21]])

teengaers = ages[ages < 18]
print(teengaers)

adults = np.where(ages >=18, ages,-1)

print(adults)


