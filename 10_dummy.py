import pandas as pd
import matplotlib.pyplot as plt
from  numpy import *
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression




data = pd.read_csv('tips.csv')
mbill = mat(data.total_bill)
mtip = mat(data.tip)
one = mat(ones(m))
X= hstack((one.T,mbill.T))





M=3
poly_features=PolynomialFeatures(degree=M, include_bias=True)
X_poly=poly_features.fit_transform(X)
model=LinearRegression()
model.fit(X_poly,tip) 




ypred=model.predict(X_poly)





SortIndex = X[:,1].argsort(0)
xsort = X[SortIndex][:,0]   

plt.scatter(data.total_bill,data.tip, color='green',s=10)
plt.plot(xsort[:,1],ypred[SortIndex], color = 'red', linewidth=3)


plt.xlabel('Total bill')
plt.ylabel('Tip')
plt.show();
