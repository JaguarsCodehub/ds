import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
np.random.seed(0)
#example data
mu=90 #mean of distribution
sigma=25 #Standard deviation of distribution
x = mu + sigma * np.random.randn(5000)
num_bins=25
fig, ax =plt.subplots()
#the histogram of the data
n, bins, patches = ax.hist(x,num_bins,density=1)
#add a 'best fit' line
y = stats.norm.pdf(bins,mu,sigma)
#mlab.normpdf(bins,mu,sigma)
ax.plot(bins,y,'--')
ax.set_xlabel('Example Data')
ax.set_ylabel('Probablity density')
sTitle=r'Histogram'+str(len(x))+'entries into'+str(num_bins)+'Bins: $\mu='+str(mu)+'$,$\sigma='+str(sigma)+'$'
ax.set_title(sTitle)
fig.tight_layout()
sPathFig='D:/Nishant/Masters/pracexam/input/DUHistogram.png'
fig.savefig(sPathFig)
plt.show()
