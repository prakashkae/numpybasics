import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

#identifying a Distribution from observed data

data_df = pd.read_csv('bball.csv',names = ['final Scores for basketball Games'], header = None)
#data_df['Final Scores for Basketball Games'].std()
data_df.hist('final Scores for basketball Games', bins = 125)
plt.ylabel('Number of Observations')
plt.show()