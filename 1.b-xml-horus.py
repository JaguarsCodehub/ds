# -*- coding: utf-8 -*-
"""
Spyder Editor

InputFileName='D:/Nishant/Masters/pracexam/Country_Code.csv'

This is a temporary script file.
"""


import pandas as pd
import xml.etree.ElementTree as ET

#=============================================================
def df2xml(data):
    header = data.columns
    root = ET.Element('root')
    
    for row in range(data.shape[0]):
        entry = ET.SubElement(root, 'entry')
        
        for index in range(data.shape[1]):
            schild = str(header[index])
            child = ET.SubElement(entry, schild)
            
            if str(data[schild][row]) != 'nan':
                child.text = str(data[schild][row])
            else:
                child.text = 'n/a'
                
    result = ET.tostring(root)
    return result

#=============================================================
def xml2df(xml_data):
    root = ET.XML(xml_data)
    all_records = []

    for i, child in enumerate(root):
        record = {}
        
        for subchild in child:
            record[subchild.tag] = subchild.text
            
        all_records.append(record)
        
    return pd.DataFrame(all_records)

#=============================================================
# Input Agreement ============================================
#=============================================================
sInputFileName='D:/Nishant/Masters/pracexam/Country_Code.xml'
InputData = open(sInputFileName).read()
print('Input Data Values ===================================')
print(InputData)

#=============================================================
# Processing Rules ===========================================
#=============================================================
ProcessDataXML = InputData
# XML to Data Frame
ProcessData = xml2df(ProcessDataXML)

# Remove columns ISO-2-Code and ISO-3-CODE
ProcessData.drop('ISO-2-CODE', axis=1, inplace=True)
ProcessData.drop('ISO-3-Code', axis=1, inplace=True)

# Rename Country and ISO-M49
ProcessData.rename(columns={'Country': 'CountryName'}, inplace=True)
ProcessData.rename(columns={'ISO-M49': 'CountryNumber'}, inplace=True)

# Set new Index
ProcessData = ProcessData.set_index('CountryNumber')

# Sort data by CountryName
ProcessData.sort_values('CountryName', axis=0, ascending=False, inplace=True)
print('Process Data Values =================================')
print(ProcessData)

#=============================================================
# Output Agreement ===========================================
#=============================================================
OutputData = ProcessData
sOutputFileName = 'D:/Nishant/Masters/pracexam/HORUS-XML-Country.csv'
OutputData.to_csv(sOutputFileName, index=False)
print('XML to HORUS - Done')