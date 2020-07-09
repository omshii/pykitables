import requests
from bs4 import BeautifulSoup
import numpy as np
import sys
import pandas
from row import Row
from wikitable import Wikitable

url = sys.argv[1]

html = requests.get(url).text

soup = BeautifulSoup(html, 'html.parser')
tables_list=soup.find_all('table', {'class': 'wikitable'})

for table in tables_list:
    rows = table.find_all('tr')
    for row in rows:\
        cells = row.find_all('td', 'th')
        for cell in cells:
            rowspan = cell.get('rowspan')
            colspan = cell.get('colspan')\
