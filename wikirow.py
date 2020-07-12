class Wikirow:

    def __init__(self):
        self.row = list()
        self.current_index = 0

    def add_cell(self, value):
        try:
            while self.row[self.current_index] is not None:
                self.current_index = self.current_index+1
            self.row[self.current_index] = value
            self.current_index = self.current_index+1
        except IndexError:
            self.row.append(None)
            self.add_cell(value)

    def insert_cell(self, value, index):
        for i in range(len(self.row), index-1):
            self.row.append(None)
        self.row.append(value)

    def to_csv(self):
        values = ""
        for val in self.row:
            values = values + str(val) + ","
        return values

    def current_len(self):
        return len(self.row)
