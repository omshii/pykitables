from row import Wikirow

class Wikitable:

    def __init__(self):
        self.table = [Row()]
        self.current_index = 0

    def add_cell(self, value):
        try:
            self.table[self.current_index].append(value)
        except IndexError:
            self.new_row()
            self.add_cell(value)

    def iterate_row(self):
        self.current_index = self.current_index + 1

    def next_add(self, value, index):
        try:
            self.table[index].append(value)
        except IndexError:
            self.new_row()
            self.next_add(value, index)

    def new_row(self):
        self.table.append(Row())

    def to_csv(self):
        csv = ""
        for row in self.table:
            csv = csv + row.get_values()
            csv = csv+'\n'
        return csv

    def current_len(self):
        return self.table[self.current_index].current_len()
