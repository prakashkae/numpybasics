import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# bar chart assignment

labels = ['A', 'B', 'C', 'D', 'E']
values = [1, 2, 3, 4, 5]

bars = plt.bar(labels, values)
plt.figure(figsize=(6,4))


bars[0].set_hatch('/')  
bars[1].set_hatch('x')
bars[2].set_hatch('o')
bars[3].set_hatch('*')
bars[4].set_hatch('\\')
plt.show()