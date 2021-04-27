import xlrd
import streamlit as st
import numpy as np
import pandas as pd
import time

def sheetByObj(sheet):
    res = []
    colsConst = {}

    for i in range(sheet.nrows): 
        rowObj = {}
        for j in range(sheet.ncols):
            cellValue = sheet.cell_value(i, j)
            if i ==0 : 
                colsConst[str(j)] = cellValue
            if i > 0:
                colName = colsConst[str(j)]
                rowObj[colName] = cellValue
        
        if i > 0:
            res.append(rowObj)
    
    return res

def mapFromExel():
    sourceExel = xlrd.open_workbook("D:\pythonws\streamlit\covid_19.xlsx")
    return sheetByObj(sourceExel.sheet_by_name("india"))

def uniqueRegions(data):
    uni = {}
    des = []
    for i in data:
        uni[i["Region"]] = i["Region"]
    for i in uni:
        des.append(i)
    return des
    
srcData = mapFromExel()
uniqueRegions = uniqueRegions(srcData)
# sourceData = mapFromExel()
# print("mapFromExel",uniqueRegions)

# Add a selectbox to the sidebar:
print("uniqueRegions",uniqueRegions)
add_selectbox = st.sidebar.selectbox('Regions', (uniqueRegions))