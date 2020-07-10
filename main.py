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

for table in tables_list:
    rows = table.find_all('tr')
    table = Wikitable()
    for row in rows:
        cells = row.find_all(['td', 'th'])
        if cells is None:
            continue
        for cell in cells:
            rowspan = cell.get('rowspan')
            colspan = cell.get('colspan')
            if colspan is None:
                colspan = 1
            if rowspan is None:
                rowspan = 1
            for i in range(int(colspan)):
                table.add_cell(cell.text.strip())
            for i in range(int(rowspan)-1):
                table.next_add(cell.text.strip(), i+1)
        table.iterate_row()
    break
