from bs4 import BeautifulSoup
import requests

HEADERS = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding":"gzip, deflate, br",
    "Accpet-Language":"en-US,en;q=0.9",
    "Connection":"keep-alive",
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.32.119 Safari/537.36",
    "Cache-Control":"max-age=0, no-cache, no-store",
    "Upgrade-Insecure-Requests":"1"
}

url = 'https://www.diamondleague.com/lists-results/statistics/'
response = requests.get(url, headers=HEADERS)
soup = BeautifulSoup(response.content, 'html.parser')

span = soup.find_all('span', class_= 'wrap')
years = []
for year in span:
    years.add(year.text)
    print(year.text)