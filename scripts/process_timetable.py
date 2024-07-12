import pandas as pd
import json
import re
import os
from datetime import datetime


def GetTableData(sheet, columnIndex):

  #print(columnIndex)





  map = {day: [] for day in dayRanges}
  for day, ranges in dayRanges.items():


    for i in range(14):

      rowIndex = ranges[0]
      value = sheet.iloc[rowIndex + (i*2), columnIndex]
      map[day].append({"Time": time[i], "Session": value if pd.notna(value) else ""})
  return map


if __name__ == '__main__':
  path = "data/TIMETABLEJANMAY2024.xlsx"
  excelData = pd.ExcelFile(path)

  data = {}
  ignoreColumns = ["DAY", "SR NO", "HOURS", "SR.NO"]
  for sheetName in excelData.sheet_names:
    sheet = pd.read_excel(path, sheet_name = sheetName, header = None)
    columns = {col: sheet.iloc[3, col] for col in range(sheet.shape[1]) if pd.notna(sheet.iloc[3, col]) and sheet.iloc[3, col] not in ignoreColumns}
    data[sheetName] = {}

    #print(sheetName)
    #print(columns.items())
    time = [t.strftime("%I:%M %p") for t in sheet.iloc[4:31:2, 2].tolist()]
    dayRanges = {
        "Monday": [4, 31 + 1],
        "Tuesday": [32, 59 + 1],
        "Wednesday": [60, 87 + 1],
        "Thursday": [88, 115 + 1],
        "Friday": [116, 143 + 1]
    }
    index = []
    name = []
    for columnIndex, className in columns.items():
      index.append(columnIndex)
      name.append(className)
      data[sheetName][className] = GetTableData(sheet, columnIndex)

  with open('data.json', 'w') as final:
    json.dump(data, final, indent = 4)