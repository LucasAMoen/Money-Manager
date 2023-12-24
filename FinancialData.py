from PdfReader import PdfReader
from SemesterData import SemesterData


class FinancialData:
    file_as_string: str
    file_path: str
    pages: str = []
    semesters: [SemesterData] = []
    notes_start_index: int

    def __init__(self):
        self.file_path = ""

    def __str__(self):
        return self.file_as_string

    def update_data(self, file_path: str):
        reader = PdfReader()
        self.pages = reader.read_pdf(file_path)
        self.file_as_string = reader.get_data_as_string()

        for n in range(len(self.pages)):
            if self.pages[n].startswith("[1]"):
                self.notes_start_index = n
                break

        cur_string = ""

        for n in range(0, self.notes_start_index):
            cur_string += self.pages[n]

        cur_string = cur_string[cur_string.find("Fall"):]

        self.semesters.append(SemesterData(cur_string[cur_string.find("Fall"):cur_string.find("Spring")]))
        cur_string = cur_string[cur_string.find("Spring"):]
        self.semesters.append(SemesterData(cur_string[cur_string.find("Spring"):]))

    def get_semesters(self):
        return self.semesters

    def print_semesters(self):
        for semester in self.semesters:
            print(semester)
