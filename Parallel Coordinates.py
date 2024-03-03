import pandas as pd
from matplotlib import pyplot as plt
Base ='C:/Users/BHAVESH/Desktop/DS_PRACS/'
sDataFile=Base+'irisdata.csv'
data = pd.read_csv(sDataFile)
from pandas.plotting import parallel_coordinates
plt.figure(figsize=(10, 10))
parallel_coordinates(data, 'Name')
sPicNameOut2=Base+'/parallel_coordinates.png'
plt.savefig(sPicNameOut2,dpi=600)
plt.tight_layout()
plt.show()