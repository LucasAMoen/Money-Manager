
class EntryData:
    def __init__(self, entry_as_string: str):
        self.entry_as_string = entry_as_string
        self.amount: float = 0
        self.note: str = ""

        self.update_data()

    def update_data(self):
        self.amount = self.entry_as_string[:self.entry_as_string.find(' ')]
        self.note = self.entry_as_string[self.entry_as_string.find(' ') + 2: len(self.entry_as_string)-1]
