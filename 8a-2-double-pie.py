import pandas as pd
import matplotlib as ml
from matplotlib import pyplot as plt
GBase ='C:/Users/Jyotindra/Desktop/DSPracs/'
ml.style.use('ggplot')
data=[
['London', 29.2, 17.4],
['Glasgow', 18.8, 11.3],
['Cape Town', 15.3, 9.0],
['Houston', 22.0, 7.8],
['Perth', 18.0, 23.7],
['San Francisco', 11.4, 33.3]
]
os_new=pd.DataFrame(data)
pd.Index(['Item', 'Value', 'Value Percent', 'Conversions', 'ConversionPercent','URL', 'StatsURL'],dtype='object')
os_new.rename(columns = {0 : "Warehouse Location"}, inplace=True)
os_new.rename(columns = {1 : "Profit 2016"}, inplace=True)
os_new.rename(columns = {2 : "Profit 2017"}, inplace=True)
explode = (0, 0, 0, 0, 0, 0)
labels=os_new['Warehouse Location']
colors_mine = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral','lightcyan','lightblue']
os_new.plot(figsize=(10, 5),kind="pie",y=['Profit 2016','Profit 2017'],autopct='%.2f%%', shadow=True, explode=explode, legend=False,colors=colors_mine,subplots=True,labels=labels,fontsize=10)
sPicNameOut2=GBase+'pie.png'
plt.savefig(sPicNameOut2, dpi=600)
print('Nishi Jain-53004230036')
