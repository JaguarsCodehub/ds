import pandas as pd
import matplotlib as ml
from matplotlib import pyplot as plt
import numpy as np
Base ='C:/Users/BHAVESH/Desktop/DS_PRACS'
ml.style.use('ggplot')
fig1=plt.figure(figsize=(10, 10))
ser = pd.Series(np.random.randn(1000))
ser.plot(figsize=(10, 10),kind='kde')
sPicNameOut1=Base+'kde.png'
plt.savefig(sPicNameOut1,dpi=600)
plt.tight_layout()
plt.show()