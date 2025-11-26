import numpy as np
filedata = np.genfromtxt('data.csv', delimiter=',')
filedata = filedata.astype('int32')

print(filedata)