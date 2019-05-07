# reading the 1D scatter plot which is important for study


import numpy as np
import seaborn as sns

iris_setosa =iris.loc(iris["species"]== "setosa"];
iris_verginica =iris.loc(iris["species"]== "virginica"];
iris_versicolor =iris.loc(iris["species"]== "versicolor"];

#print(iris_setosa["petalLength"])

plt.plot(iris_setosa["PetalLength"], np.zeros_like(iris_setosa['PetalLength']);
plt.plot(iris_virginica["PetalLength"], np.zeros_like(iris_virginica['PetalLength']);
plt.plot(iris_versicolor["PetalLength"], np.zeros_like(iris_versicolor['PetalLength']);

plt.show();
 
# Disadvantages of 1D Scatter plot is
# 1. Overlapping of lot of points
# 2. We need to discover better ways to visualize the 1 D Scatter plot.


sns.FacetGrid(iris hue="specis", size =5) \
   . map(sns.distplot, "PetalLength") \
   .add_legend();
   
plt.show();