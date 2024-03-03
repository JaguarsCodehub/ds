import pandas as pd
from matplotlib import pyplot as plt
Base ='C:/Users/BHAVESH/Desktop/DS_PRACS/'
sDataFile=Base+'irisdata.csv'
data = pd.read_csv(sDataFile)
from pandas.plotting import andrews_curves
plt.figure(figsize=(10, 10))
andrews_curves(data, 'Name')
sPicNameOut1=Base+'/andrews_curves.png'
plt.savefig(sPicNameOut1,dpi=600)
plt.tight_layout()
plt.show()