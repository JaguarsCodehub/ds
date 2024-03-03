import pandas as pd
from matplotlib import style
from matplotlib import pyplot as plt
import numpy as np
Base ='C:/Users/BHAVESH/Desktop/DS_PRACS/'
style.use('ggplot')
from pandas.plotting import autocorrelation_plot
plt.figure(figsize=(10, 10))
data = pd.Series(0.7 * np.random.rand(1000) + 0.3 * np.sin(np.linspace(-9 * np.pi, 9 * np.pi, num=1000)))
autocorrelation_plot(data)
sPicNameOut2=Base+'/autocorrelation_plot.png'
plt.savefig(sPicNameOut2,dpi=600)
plt.tight_layout()
plt.show()