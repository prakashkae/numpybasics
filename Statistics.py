
import numpy as np

#calculate mean, median, mode, standard deviation, variance

driv_speed_mph= [39,31,45,27,58,26,54,35,51,53]

mean1 = np.mean(driv_speed_mph)
print(mean1)

median1 = np.median(driv_speed_mph)
print(median1)


from statistics import mode

mode1 = mode(driv_speed_mph)
print(mode1)

std1 = np.std(driv_speed_mph)
print(std1)

var1 = np.var(driv_speed_mph)
print(var1)
