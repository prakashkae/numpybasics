import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from scipy import stats

plt.rcParams['figure.figsize'] = (12,10)
plt.rcParams['font.size'] = 15


#unifrom distribution

plt.hist(stats.uniform.rvs(size = 1000),edgecolor = 'black', color='lightgreen')
plt.title(r'Uniform Distribution $U \sim U(0,1)$')
plt.ylabel('Number of Observations')
#plt.show()

fig, axs = plt.subplots(4)
fig.suptitle('Poisson Distribution')
fig.tight_layout(rect=[0,0.03,1,0.95])
color_list = ['lightgreen','lightblue','lightcoral','yellowgreen']
bins = np.arange(0,11)-0.5

for i,j in zip(range(4),color_list):
    axs[i].hist(stats.poisson.rvs(mu=i,size=100),edgecolor='black',color=j,bins=bins)
    axs[i].set_title(r'Poisson Distribution $\lambda = $'+str(i))
    axs[i].set_ylabel('Number of Observations')


fig.legend(bbox_to_anchor=(1,0.92), loc='upper left')

plt.show()