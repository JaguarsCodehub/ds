# InputFileName='D:/Nishant/Masters/pracexam/Country_Code.csv'
"""
Spyder Editor

InputFileName='D:/Nishant/Masters/pracexam/Country_Code.csv'

This is a temporary script file.
"""


!pip install scikit-fuzzy
from matplotlib.pyplot import imread
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
sInputFileName='D:/Nishant/Masters/pracexam/Angus.jpg'
InputData = imread(sInputFileName)
print('Input Data Values ===================================')
print('X: ',InputData.shape[0])
print('Y: ',InputData.shape[1])
print('RGBA: ', InputData.shape[2])
print('=====================================================')
ProcessRawData=InputData.flatten()
y=InputData.shape[2] + 3
x=int(ProcessRawData.shape[0]/y)
ProcessData=pd.DataFrame(np.reshape(ProcessRawData, (x, y)))
sColumns= ['XAxis','YAxis','Red', 'Green', 'Blue','Alpha']
ProcessData.columns=sColumns
ProcessData.index.names =['ID']
print('Rows: ',ProcessData.shape[0])
print('Columns :',ProcessData.shape[1])
print('=====================================================')
print('Process Data Values =================================')
print('=====================================================')
plt.imshow(InputData)
plt.show()
print('=====================================================')
OutputData=ProcessData
print('Storing File')
sOutputFileName='D:/Nishant/Masters/pracexam/HORUS-Picture.csv'
OutputData.to_csv(sOutputFileName, index = False)
print('Picture to HORUS - Done')