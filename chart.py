import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# bar chart assignment

labels = ['A', 'B', 'C', 'D', 'E']
values = [1, 2, 3, 4, 5]

plt.bar(labels, values)
plt.figure(figsize=(6,4))
plt.show()
