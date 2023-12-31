import re
import camelot
import pdfplumber
import pandas as pd
from pypdf import PdfReader

pdf = 'results_pdfs/Brussels_2023_results.pdf'

reader = PdfReader(pdf)
number_of_pages = len(reader.pages)
page = reader.pages[0]
data = page.extract_text()

lines = data.split('\n')

# print(lines)

data_rows = []
current_data = {}
header = None

# Define regular expressions to match patterns
reaction_pattern = re.compile(r'\b\d+\.\d{3}\b')
date_pattern = re.compile(r'^\d{1,2} [A-Za-z]{3} \d{4}$')
# name_pattern = re.compile(r'^(?:[a-zA-Z]{2,15} ?\b){2,3}$')
name_pattern = re.compile
result_pattern = re.compile(r'(\d+:\d+\.\d+)|(\d+\.\d+)|DNF')
nat_pattern = re.compile(r'^[A-Z]{3}$')

# Iterate through the lines
for line in lines:
    if line.isdigit():
        # This line is a rank, skip it
        current_data['Rank'] = line
        current_data['Lane'] = line
    elif date_pattern.match(line):
        # This line is a Date of Birth
        current_data['Date of Birth'] = line

    elif name_pattern.match(line):
        current_data['Name'] = line

    elif nat_pattern.match(line):
        current_data['Nat'] = line
    
    elif reaction_pattern.match(line):
        current_data['Reaction_Time'] = line

    elif result_pattern.match(line):
        current_data['Result'] = line

    else:
        current_data['extras'] = line
        data_rows.append(current_data.copy())

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(data_rows)
df = df[~(df['Name'].isin(df.columns))]

print(df)