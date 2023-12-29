from PdfReader import PdfReader
from SemesterData import SemesterData


class FinancialData:
    file_as_string: str
    file_path: str
    pages: str = []
    semesters: [SemesterData] = []
    notes_start_index: int

    number_of_notes: int

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

        page = self.pages[self.notes_start_index - 1]

        self.number_of_notes = int(page[page.rfind("[") + 1:page.rfind("]")])

        cur_string = ""

        for n in range(0, self.notes_start_index):
            cur_string += self.pages[n]

        for num in range(1, self.number_of_notes + 1):

            to_replace = '[' + cur_string[cur_string.find('[' + str(num) + ']') + 1:
                                          cur_string.find('[' + str(num) + ']') + 1 + len(str(num))] + ']'
            end_substring_index = self.file_as_string.rfind('[' + str(num+1) + ']') - 1
            if end_substring_index == -1:
                end_substring_index = len(self.file_as_string)

            replacement = self.file_as_string[self.file_as_string.rfind('[' + str(num) + ']') + len(str(num)) + 3:
                                              end_substring_index]

            replacement = replacement.replace('\n', ' ')

            cur_string = cur_string.replace(to_replace, '[' + replacement + ']')

        cur_string = cur_string[cur_string.find("Fall"):]

        self.semesters.append(SemesterData(cur_string[cur_string.find("Fall"):cur_string.find("Spring")]))
        cur_string = cur_string[cur_string.find("Spring"):]
        self.semesters.append(SemesterData(cur_string[cur_string.find("Spring"):]))

    def get_semesters(self):
        return self.semesters

    def print_semesters(self):
        for semester in self.semesters:
            print(semester)
