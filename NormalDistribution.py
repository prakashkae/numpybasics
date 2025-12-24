import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats



#normal distribution

mean = 0
variance = 1
std_dev = variance ** 0.5
norm_samples = np.random.normal(size = 1000)


plt.hist(norm_samples, density=True, color='lightblue', edgecolor='black', label=f'$\overline{{x}} = {np.mean(norm_samples):0.3f}$\n$s = {np.std(norm_samples):0.3f}$')
xmin,xmax = plt.xlim()
x = np.linspace(mean - 4*std_dev,mean + 4*std_dev,1000)
p = stats.norm.pdf(x,mean,std_dev)
plt.plot(x,p,linewidth=2,color='purple',label='Standard Normal Distribution')

plt.legend()
plt.show()