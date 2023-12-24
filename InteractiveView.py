from tkinter import *
from tkinter import filedialog

import ttkbootstrap as tb
from FinancialData import FinancialData
from SemesterData import SemesterData
from WeekData import WeekData


class InteractiveView:
    def __init__(self):
        self.root = tb.Window(themename="superhero")

        self.root.title("Money Manager")
        self.root.geometry("750x500")

        self.financial_data: FinancialData = FinancialData()

        self.week_data = None
        self.semester: SemesterData
        self.weeks: [WeekData] = []

        self.add_title()
        self.add_buttons()
        self.add_week_data()

        self.root.mainloop()

    def update_weeks(self):
        self.weeks = []
        self.week_data.delete()
        for week in self.semester.get_weeks():
            week: WeekData = week
            self.weeks.append((f'Week {week.week_number + 1}', f'{week.start_date}', f'{week.total}'))
        for week in self.weeks:
            self.week_data.insert('', END, values=week)

    def change_to_fall(self):
        if len(self.financial_data.semesters) > 1:
            self.semester = self.financial_data.semesters[0]
            self.update_weeks()

    def change_to_spring(self):
        if len(self.financial_data.semesters) > 1:
            self.semester = self.financial_data.semesters[1]
            self.update_weeks()

    def browse_files(self):
        file_path = filedialog.askopenfilename(initialdir="C:\\Users\\lucas\\",
                                               title="Select a File",
                                               filetypes=[("PDF Files", "*.pdf*")])
        if file_path != "":
            self.financial_data.update_data(file_path)
            self.change_to_fall()

    def add_title(self):
        title_text = tb.Label(self.root, text="Money Manager", font=("Helvetica", 24))
        title_text.pack()

    def add_buttons(self):
        button_frame = tb.Frame(self.root)
        button_frame.pack()

        fall_button = tb.Button(button_frame, text="Fall", command=self.change_to_fall)
        fall_button.pack(side=tb.LEFT)
        spring_button = tb.Button(button_frame, text="Spring", command=self.change_to_spring)
        spring_button.pack(side=tb.LEFT)

        browse_files_button = tb.Button(button_frame, text="Browse Files", command=self.browse_files)
        browse_files_button.pack(side=tb.RIGHT)

    def add_week_data(self):
        columns = ("week", "date", "total")

        self.week_data = tb.Treeview(self.root, style="success", columns=columns,
                                     show="headings")

        self.week_data.pack(fill=tb.BOTH, expand=1)

        self.week_data.heading("week", text="Week")
        self.week_data.heading("date", text="Date")
        self.week_data.heading("total", text="Total Spent")
