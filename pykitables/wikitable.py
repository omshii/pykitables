from pykitables.wikirow import Wikirow

class Wikitable:

    def __init__(self):
        self.table = [Wikirow()]
        self.current_index = 0

    def add_value(self, value):
        try:
            self.table[self.current_index].add_cell(value)
        except IndexError:
            self.new_row()
            self.add_value(value)

    def iterate_row(self):
        self.current_index = self.current_index + 1

    def next_add(self, value, index):
        for i in range(len(self.table)-1, self.current_index+index):
            self.new_row()
        self.table[self.current_index+index].insert_cell(value, self.current_len())

    def new_row(self):
        self.table.append(Wikirow())

    def to_csv(self):
        csv = ""
        for row in self.table:
            csv = csv + row.to_csv()
            csv = csv+'\n'
        return csv

    #TODO: messy, replace with get current row perhaps
    def current_len(self):
        return self.table[self.current_index].current_len()
