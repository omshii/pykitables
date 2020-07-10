class Wikirow:

    def __init__(self):
        self.row = list()
        self.current_index = 0

    def append(self, value):
        self.row.append(value)

    def get_values(self):
        values = ""
        for val in self.row:
            values = values + str(val) + ","
        return values

    def current_len(self):
        return len(self.row)
