from PyPDF2 import PdfFileReader
from shutil import move

PAPER_DIR = 'acl_2016/'

for i in range(1, 232):
    file_path = PAPER_DIR + str(i).rjust(3, '0') + '.pdf'

    pdf_reader = PdfFileReader(open(file_path, 'rb'))
    paper_title = str(pdf_reader.getDocumentInfo().title)

    paper_title = paper_title.replace('/', ' ')
    new_file_path = PAPER_DIR + paper_title + '.pdf'
    move(file_path, new_file_path)
