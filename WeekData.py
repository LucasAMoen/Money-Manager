import time


class WeekData:
    def __init__(self, week_as_string: str):
        self.week_as_string = week_as_string
        self.week_number = 0
        self.start_date = ""
        self.total = 0
        self.entries = []

        self.update_data()

    def set_week_number(self, week_number: int):
        self.week_number = week_number

    def update_data(self):
        cur_string = self.week_as_string

        self.start_date = cur_string[0:cur_string.find(' ')]
        cur_string = cur_string[cur_string.find(' ')+1:]

        if cur_string.isnumeric():
            self.total = float(cur_string)

        if cur_string.find(' ') != -1:
            self.total = float(cur_string[0:cur_string.find(' ')])
            cur_string = cur_string[cur_string.find(' ')+1:]
