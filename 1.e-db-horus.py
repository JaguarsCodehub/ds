# InputFileName='D:/Nishant/Masters/pracexam/Country_Code.csv'
"""
Spyder Editor

InputFileName='D:/Nishant/Masters/pracexam/Country_Code.csv'

This is a temporary script file.
"""


import pandas as pd
import sqlite3 as sq
sInputFileName='D:/Nishant/Masters/pracexam/utility.db'
sInputTable='Country_Code'
conn = sq.connect(sInputFileName)
sSQL='select * FROM ' + sInputTable + ';'
InputData=pd.read_sql_query(sSQL, conn)
print('Input Data Values ===================================')
print(InputData)
print('=====================================================')
ProcessData=InputData
ProcessData.drop('ISO-2-CODE', axis=1,inplace=True)
ProcessData.drop('ISO-3-Code', axis=1,inplace=True)
ProcessData.rename(columns={'Country': 'CountryName'}, inplace=True)
ProcessData.rename(columns={'ISO-M49': 'CountryNumber'}, inplace=True)
ProcessData.set_index('CountryNumber', inplace=False)
ProcessData.sort_values('CountryName', axis=0, ascending=False, inplace=True)
print('Process Data Values =================================')
print(ProcessData)
print('=====================================================')
OutputData=ProcessData
sOutputFileName='D:/Nishant/Masters/pracexam/db-Horus.csv'
OutputData.to_csv(sOutputFileName, index = False)
print('Database to HORUS - Done')