import pandas as pd
import matplotlib as ml
from matplotlib import pyplot as plt
import numpy as np
Base ='C:/Users/BHAVESH/Desktop/DS_PRACS'
ml.style.use('ggplot')
fig2=plt.figure(figsize=(10, 10))
from pandas.plotting import scatter_matrix
df = pd.DataFrame(np.random.randn(1000, 5), columns=['Y2014','Y2015','Y2016', 'Y2017',
'Y2018'])
scatter_matrix(df, alpha=0.2, figsize=(10, 10), diagonal='kde')
sPicNameOut2=Base+'scatter_matrix.png'
plt.savefig(sPicNameOut2,dpi=600)
plt.tight_layout()
plt.show()
