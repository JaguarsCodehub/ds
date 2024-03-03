import pandas as pd
import xml.etree.ElementTree as ET

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

# Input Agreement ============================================
sInputFileName='C:/Users/Jyotindra/Desktop/DSPracs/Country_Code.xml'
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
sOutputFileName = 'C:/Users/Jyotindra/Desktop/DSPracs/HORUS-XML-Country.csv'
OutputData.to_csv(sOutputFileName, index=False)
print('XML to HORUS - Done')