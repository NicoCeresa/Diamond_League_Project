import re
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

folder_name='results_pdfs'
if not os.path.exists(folder_name):
    os.mkdir(folder_name)


url = 'https://www.diamondleague.com/lists-results/2023-results/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

pattern = re.compile(r'(.+?) 2023: Results \(PDF\)')

# Find all elements that match the pattern
section_titles = soup.find_all('a', text=pattern)

for title_element in section_titles:
    # Extract the section title
    section_title = pattern.search(title_element.text).group(1)

    # Extract the PDF link
    pdf_link = title_element['href']

    # Create the full URL for the PDF
    full_pdf_url = urljoin(url, pdf_link)

    # Send a GET request to download the PDF file
    pdf_response = requests.get(full_pdf_url)

    if pdf_response.status_code == 200:
        # Save the PDF file with a name based on the section title, inside the folder
        pdf_filename = os.path.join(folder_name, f'{section_title}_2023_results.pdf')
        with open(pdf_filename, 'wb') as pdf_file:
            pdf_file.write(pdf_response.content)
        print(f'PDF for "{section_title}" downloaded and saved to "{pdf_filename}"')
    else:
        print(f'Failed to download the PDF for "{section_title}".')





