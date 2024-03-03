#'D:/Nishant/Masters/pracexam/input/

import sqlite3 as sq
import pandas as pd
Base='D:/Nishant/Masters/pracexam/input/'
sDatabaseName=Base + 'vermeulen.db'
conn = sq.connect(sDatabaseName)
sFileName=Base + 'Retrieve_IP_DATA.csv'
print('Loading :',sFileName)
IP_DATA_ALL_FIX=pd.read_csv(sFileName,header=0,low_memory=False)
IP_DATA_ALL_FIX.index.names = ['RowIDCSV']
sTable='IP_DATA_ALL'
print('Storing :',sDatabaseName,' Table:',sTable)
IP_DATA_ALL_FIX.to_sql(sTable, conn, if_exists='replace')
print('Loading :',sDatabaseName,'Table:',sTable)
TestData=pd.read_sql_query("select * from IP_DATA_ALL;", conn)
print('################')
print('Data Values')
print(TestData)
print('\nData Profile')
print('\nRows :',TestData.shape[0])
print('Columns :',TestData.shape[1])
print('Done!!')
