from bs4 import BeautifulSoup
import requests
from datetime import datetime
import os
import pandas as pd
import numpy as np

HEADERS = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding":"gzip, deflate, br",
    "Accpet-Language":"en-US,en;q=0.9",
    "Connection":"keep-alive",
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.32.119 Safari/537.36",
    "Cache-Control":"max-age=0, no-cache, no-store",
    "Upgrade-Insecure-Requests":"1"
}

main_url = 'https://www.diamondleague.com/lists-results/statistics/'

# response = requests.get(url, headers=HEADERS)
# soup = BeautifulSoup(response.content, 'html.parser')

years = [year for year in range(2010, datetime.now().year + 1)]

# for year in years:
year = 2013
url = f'https://dl.all-athletics.com/dls/en/seasons-list/{year}/ffnnn/10229630/1073741823/detailed'
response = requests.get(url, headers=HEADERS)
soup = BeautifulSoup(response.content, 'html.parser')

# results_panel = soup.find_all('th')
# results_list = np.array([result.text for result in results_panel])

columns = soup.find_all('th')

result = soup.find_all('td', class_='right result')
wind = soup.find_all('td', class_='right wind')
pa = soup.find_all('td', class_='center')
pr = soup.find_all('td', class_='center')
Athlete = soup.find_all('td', class_='left achiever')
Birth = soup.find_all('td', class_='center birthdate')
Nat = soup.find_all('td', class_='center nationality')
Race = soup.find_all('td', class_='right')
place = soup.find_all('td', class_='center place')
venue = soup.find_all('td', class_='venue')
date = soup.find_all('td', class_='date')
rs = soup.find_all('td', class_='center score')
rec = soup.find_all('td', class_='center')

# results_df = pd.DataFrame(columns=columns, data=results_list)
# results_df.head()
# results_list.to_csv(os.path.join('diamond_league/test_files', 'uncleaned_test.csv'))
print([column.text for column in result])