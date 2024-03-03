# InputFileName='D:/Nishant/Masters/pracexam/Country_Code.csv'
"""
Spyder Editor

InputFileName='D:/Nishant/Masters/pracexam/Country_Code.csv'

This is a temporary script file.
"""


import pandas as pd
sInputFileName='D:/Nishant/Masters/pracexam/Country_Code.json'
InputData=pd.read_json(sInputFileName,orient='index',encoding="latin-1")
print('Input Data Values')
print(InputData)
ProcessData=InputData
ProcessData.drop('ISO-2-CODE',axis=1,inplace=True)
ProcessData.drop('ISO-3-Code',axis=1,inplace=True)
ProcessData.rename(columns={'Country':'CountryName'},inplace=True)
ProcessData.rename(columns={'ISO-M49':'CountryNumber'},inplace=True)
#Set new Index
ProcessData.set_index('CountryNumber',inplace=False)
#Sort data by currency number
ProcessData.sort_values('CountryName',axis=0,ascending=False,inplace=True)
print('Process Data Values')
print(ProcessData)
OutputData=ProcessData
sOutputFileName='D:/Nishant/Masters/pracexam/HORUS-JSON-Country.csv'
OutputData.to_csv(sOutputFileName,index=False)
print('JSON to HORUS-Done')