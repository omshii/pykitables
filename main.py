#TODO: Get links
#TODO: Build package

import requests
from bs4 import BeautifulSoup
import numpy as np
import sys
import pandas
from table import Wikitable

url = sys.argv[1]

html = requests.get(url).text

soup = BeautifulSoup(html, 'html.parser')
tables_list=soup.find_all('table', {'class': 'wikitable'})

i = 0

for table in tables_list:
    rows = table.find_all('tr')
    wikitable = Wikitable()
    for row in rows:
        cells = row.find_all(['td', 'th'])
        if cells is None: #TODO?
            continue
        for cell in cells:
            rowspan = cell.get('rowspan')
            colspan = cell.get('colspan')
            value = cell.text.strip()
            if ',' in value or '\n' in value:
                value = '"'+value+'"'
            if colspan is None:
                colspan = 1
            if rowspan is None:
                rowspan = 1
            for m in range(int(colspan)):
                wikitable.add_value(value)
            for n in range(int(rowspan)-1):
                wikitable.next_add(value, n+1)
        wikitable.iterate_row()
    with open('table'+str(i), 'w') as outfile:
        outfile.write(wikitable.to_csv())
    i = i+1
