import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#percent changes

a = pd.Series([2,1,3,3,4,5])

#print(a)
#print(a.pct_change())

df = pd.DataFrame(
    {
        'A':a,
        'B':a**2
    }
)

#print(df)
#print(df.pct_change(periods=2))


#covariance

b = pd.Series([4,5,5,7,8,6])
#print(b)

df1 = pd.DataFrame({
    'A':a,
    'A1':a**2,
    'B':b,
    'B1':b**2
})

#print(df1)
#print(a.cov(b))

#print(df1.cov())

#print(np.sum((a-np.mean(a))**2/(len(a)-1)))

df1.iloc[2:4, 0:2] = np.nan
df1.iloc[3:5, 2:4] = np.nan
#print(df1.cov(min_periods=3))


#correlation

#print(a.corr(b))

#print(a.corr(b, method='pearson'))

#print(a.corr(b, method='kendall'))

#plt.scatter(a,b)
#plt.show()66
#print(df1['A'].corr(df1['B']))

#plt.show()

#print(df1)

#print(df1['A'].corr(df1['B'],min_periods=2))   


# using a custom function with correlation

#print(df1)

def calc_cov(x,y):
    t1 = (x-np.mean(x))
    t2 = (y-np.mean(y))
    tcov = np.sum(t1*t2)/(len(x)-1)
    print(x,y,t1,t2,tcov)
    print('___________')
    return tcov

print(df1.corr(method=calc_cov))    


#corrwith()

df2 = df1.copy()**2
print(df2)
print(df2.corrwith(df1))

print(df2.A.corr(df1.A, method='pearson'))
