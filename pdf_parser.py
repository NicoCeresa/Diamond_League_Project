import re
import tabula
from tabula import read_pdf
from pdfquery import PDFQuery
from pdfminer.high_level import extract_pages, extract_text

tables = tabula.read_pdf('results_pdfs/Brussels_2023_results.pdf')
print(tables)

# for page_layout in extract_pages('results_pdfs/Brussels_2023_results.pdf'):
#     for element in page_layout:
#         # print(element)
#         pass

# text = extract_text('results_pdfs/Brussels_2023_results.pdf')

# pattern = re.compile(r"")

# pdf = PDFQuery('results_pdfs/Brussels_2023_results.pdf')
# pdf.load()

# # Use CSS-like selectors to locate the elements
# text_elements = pdf.pq('LTTextLineHorizontal')

# # Extract the text from the elements
# text = [t.text for t in text_elements]

# print(text)