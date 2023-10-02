import camelot

pdf = 'results_pdfs/Brussels_2023_results.pdf'

tables = camelot.read_pdf(pdf)
print(tables)
