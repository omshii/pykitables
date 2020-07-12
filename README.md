# pykitables
A python package for getting all the tables from a Wikipedia page.


## Usage
``` import pykitables
    tables = pykitables.get_tables("https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data/United_States_medical_cases")
    #Returns a list of Wikitable objects
    csv1 = tables[0].to_csv()
    #Returns the csv for the first table in the article
```
