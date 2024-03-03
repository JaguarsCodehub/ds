import pandas as pd
from matplotlib import style
from matplotlib import pyplot as plt
import numpy as np
Base ='C:/Users/BHAVESH/Desktop/DS_PRACS/'
style.use('ggplot')
from pandas.plotting import lag_plot
plt.figure(figsize=(10, 10))
data = pd.Series(0.1 * np.random.rand(1000) + \
0.9 * np.sin(np.linspace(-99 * np.pi, 99 * np.pi, num=1000)))
lag_plot(data)
sPicNameOut1=Base+'/lag_plot.png'
plt.savefig(sPicNameOut1,dpi=600)
plt.tight_layout()
plt.show()