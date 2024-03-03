import pandas as pd
from matplotlib import style
from matplotlib import pyplot as plt
import numpy as np
Base ='C:/Users/BHAVESH/Desktop/DS_PRACS/'
style.use('ggplot')
from pandas.plotting import bootstrap_plot
data = pd.Series(np.random.rand(1000))
plt.figure(figsize=(10, 10))
bootstrap_plot(data, size=50, samples=500, color='grey')
sPicNameOut3=Base+'/bootstrap_plot.png'
plt.savefig(sPicNameOut3,dpi=600)
plt.tight_layout()
plt.show()