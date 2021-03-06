import io
import os
import csv
import json
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage

PDF_NAME_LIST = []
PDF_LIST = []
DATA_DICT = {}
PATH = "your/path/here/"
OUTPUT = open("PDF_Dict.txt", "w")

# Gather all PDFs into a list
for file in os.listdir(PATH):
    PDF_LIST.append(file)

# Gather all PDFs without '.pdf' - probably a waste of space but helpful for now to keep text clean
for file in PDF_LIST:
    file = file[:-4]
    PDF_NAME_LIST.append(file)


def extract_text_from_pdf(pdf_path):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)
    
    #Utilizing PDF miner module to read each page of the current PDF
    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh,
                                      caching=True,
                                      check_extractable=True):
            page_interpreter.process_page(page)

        text = fake_file_handle.getvalue()

    # close open handles
    converter.close()
    fake_file_handle.close()

    if text:
        return text


total = len(PDF_LIST)

if __name__ == '__main__':

    for i in range(len(PDF_LIST)):

        DATA_DICT[PDF_NAME_LIST[i]
                  ] = extract_text_from_pdf(PATH + PDF_LIST[i])
        
        #Progress output in terminal
        print(i+1, " | ", total, " | ", PDF_NAME_LIST[i])

    OUTPUT.write(json.dumps(DATA_DICT))
    print("Completed")
