import pandas as pd
from matplotlib import pyplot as plt
Base ='C:/Users/BHAVESH/Desktop/DS_PRACS/'
sDataFile=Base+'irisdata.csv'
data = pd.read_csv(sDataFile)
from pandas.plotting import radviz
plt.figure(figsize=(10, 10))
radviz(data, 'Name')
sPicNameOut3=Base+'/radviz.png'
plt.savefig(sPicNameOut3,dpi=600)
plt.tight_layout()
plt.show()