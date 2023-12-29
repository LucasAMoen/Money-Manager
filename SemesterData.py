from WeekData import WeekData


class SemesterData:
    def __init__(self, semester_as_string: str):
        self.total_spending = 0
        self.weeks: [WeekData] = []
        self.semester_as_string = semester_as_string

        self.update_data()

    def __str__(self):
        return self.semester_as_string

    def get_weeks(self) -> [WeekData]:
        return self.weeks

    def update_data(self):
        cur_string = self.semester_as_string
        lines = cur_string.split('\n')

        for n in range(0, 2):
            lines.remove(lines[0])

        self.total_spending = float(lines[0][(lines[0].find("Start Date") + len("Start Date")):])
        lines.remove(lines[0])

        for n in range(0, len(lines)):
            week_to_add = WeekData(lines[n])
            week_to_add.set_week_number(n)
            self.weeks.append(week_to_add)
