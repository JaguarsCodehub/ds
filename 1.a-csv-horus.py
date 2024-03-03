import pandas as pd
#input agreement===========================================
sInputFileName='C:/Users/Jyotindra/Desktop/DSPracs/Country_Code.csv'
InputData=pd.read_csv(sInputFileName, encoding="latin-1")
print('Input Data Values====================')
print(InputData)
print('=====================')
#Processing Rules==========================================
ProcessData=InputData
#remove columns ISO-2-code and ISO-3-code==================
ProcessData.drop('ISO-2-CODE',axis=1,inplace=True)
ProcessData.drop('ISO-3-Code',axis=1,inplace=True)
#rename Country and ISO-M49================================
ProcessData.rename(columns={'Country':'CountryName'},inplace=True)
ProcessData.rename(columns={'ISO-M49':'CountryNumber'},inplace=True)
#set new Index=============================================
ProcessData.set_index('CountryNumber',inplace=False)
#sort data by CurrencyNumber===============================
ProcessData.sort_values('CountryName',axis=0,ascending=False,inplace=True)
print('Process Data Values')
print(ProcessData)
#Output Agreement==========================================
OutputData=ProcessData
sOutputFileName='C:/Users/Jyotindra/Desktop/DSPracs/HORUS-CSV-Country.csv'
OutputData.to_csv(sOutputFileName,index=False)
print('CSV to HORUS - Done')
