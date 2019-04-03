from PyPDF2 import PdfFileReader
from shutil import move
import os

PAPER_DIR = '../../acl_2018/'

for file in os.listdir(PAPER_DIR):
    if ".pdf" not in file:
        continue
    file_path = "{}{}".format(PAPER_DIR, file)
    pdf_reader = PdfFileReader(open(file_path, 'rb'))
    paper_title = str(pdf_reader.getDocumentInfo().title)

    paper_title = paper_title.replace('/', ' ')
    new_file_path = PAPER_DIR + paper_title + '.pdf'
    move(file_path, new_file_path)
