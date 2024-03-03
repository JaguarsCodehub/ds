import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
def show_info(aname, a,r):
 print ('----------------')
 print ("Audio:", aname)
 print ('----------------')
 print ("Rate:", r)
 print ('----------------')
 print ("shape:", a.shape)
 print ("dtype:", a.dtype)
 print ("min, max:", a.min(), a.max())
 print ('----------------')
 plot_info(aname, a,r)
def plot_info(aname, a,r):
 sTitle= 'Signal Wave - '+ aname + ' at ' + str(r) + 'hz'
 plt.title(sTitle)
 sLegend=[]
 for c in range(a.shape[1]):
     sLabel = 'Ch' + str(c+1)
     sLegend=sLegend+[str(c+1)]
     plt.plot(a[:,c], label=sLabel)
 plt.legend(sLegend)
 plt.show()
sInputFileName='D:/Nishant/Masters/pracexam/2ch-sound.wav'
print('=====================================================')
print('Processing : ', sInputFileName)
print('=====================================================')
InputRate, InputData = wavfile.read(sInputFileName)
show_info("2 channel", InputData,InputRate)
ProcessData=pd.DataFrame(InputData)
sColumns= ['Ch1','Ch2']
ProcessData.columns=sColumns
OutputData=ProcessData
sOutputFileName='D:/Nishant/Masters/pracexam/HORUS-Audio-2ch.csv'
OutputData.to_csv(sOutputFileName, index = False)
sInputFileName='D:/Nishant/Masters/pracexam/4ch-sound.wav'
print('=====================================================')
print('Processing : ', sInputFileName)
print('=====================================================')
InputRate, InputData = wavfile.read(sInputFileName)
show_info("4 channel", InputData,InputRate)
ProcessData=pd.DataFrame(InputData)
sColumns= ['Ch1','Ch2','Ch3', 'Ch4']
ProcessData.columns=sColumns
OutputData=ProcessData
sOutputFileName='D:/Nishant/Masters/pracexam/HORUS-Audio-4ch.csv'
OutputData.to_csv(sOutputFileName, index = False)
sInputFileName='D:/Nishant/Masters/pracexam/6ch-sound.wav'
print('=====================================================')
print('Processing : ', sInputFileName)
print('=====================================================')
InputRate, InputData = wavfile.read(sInputFileName)
show_info("6 channel", InputData,InputRate)
ProcessData=pd.DataFrame(InputData)
sColumns= ['Ch1','Ch2','Ch3', 'Ch4', 'Ch5','Ch6']
ProcessData.columns=sColumns
OutputData=ProcessData
sOutputFileName='D:/Nishant/Masters/pracexam/HORUS-Audio-6ch.csv'
OutputData.to_csv(sOutputFileName, index = False)
sInputFileName='D:/Nishant/Masters/pracexam/8ch-sound.wav'
print('=====================================================')
print('Processing : ', sInputFileName)
print('=====================================================')
InputRate, InputData = wavfile.read(sInputFileName)
show_info("8 channel", InputData,InputRate)
ProcessData=pd.DataFrame(InputData)
sColumns= ['Ch1','Ch2','Ch3', 'Ch4', 'Ch5','Ch6','Ch7','Ch8']
ProcessData.columns=sColumns
OutputData=ProcessData
sOutputFileName='D:/Nishant/Masters/pracexam/HORUS-Audio-8ch.csv'
OutputData.to_csv(sOutputFileName, index = False)
print('Audio to HORUS - Done')