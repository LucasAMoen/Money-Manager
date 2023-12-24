import PyPDF2


class PdfReader:
    def __init__(self):
        self.file = None
        self.data_as_string = ""
        self.number_of_pages = 0
        self.pages = []

    def read_pdf(self, file_path=""):
        try:
            my_file = open(file_path, 'rb')
        except IOError:
            print("File Not Found")
            return
        pdf_reader = PyPDF2.PdfReader(my_file)

        self.number_of_pages = len(pdf_reader.pages)

        for i in range(0, self.number_of_pages):
            self.pages.append(pdf_reader.pages[i].extract_text())
            self.data_as_string = self.data_as_string + pdf_reader.pages[i].extract_text()

        self.file = my_file

        return self.pages

    def get_data_as_string(self):
        return self.data_as_string

    def print_data(self):
        for i in range(0, self.number_of_pages):
            print(self.pages[i])
