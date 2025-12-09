import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#basic 
x = [0,1,2,3,4]
y = [0,2,4,6,8]
#plt.plot(x,y, label="2x" , color="red", linewidth=2,marker="o"    , markersize=10, markerfacecolor="blue", markeredgewidth=2, markeredgecolor="green")

#use shothand notation
plt.plot(x,y, 'b^--', label="2x")
plt.plot(x2,x2**2)
# line nubmer two

x2 = np.arange(0,4.5,0.5)
print(x2)
plt.title(
    "My first graph" , fontdict={"fontname":"Comic Sans MS", "fontsize":20}
)
plt.xlabel("X axis", fontdict={"fontname":"Comic Sans MS", "fontsize":20})
plt.ylabel("Y axis")


#line number two


plt.xticks([0,1,2,3,4])
plt.yticks([0,2,4,6,8])
plt.legend()
plt.show()