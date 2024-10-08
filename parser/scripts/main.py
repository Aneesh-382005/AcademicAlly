import datetime
from openpyxl import load_workbook
from collections import defaultdict
import json
import os
import sys


from parser.scripts.utillities import parser

def main():
    workbook = load_workbook('../utilities/TimeTable[1].xlsx')
    result = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: None)))
    for sheet in workbook.worksheets:
        print(sheet.title)
        parser(sheet, result)


    file_path = '../result(parsedOnly).json'
    with open(file_path, 'w') as file:
        json.dump(result, file, indent=4, separators=(',', ': '))

if __name__ == "__main__":
    main()
