import os
import requests
import numpy as np
import pandas as pd
from glob import glob
from datetime import datetime as date
from bs4 import BeautifulSoup

HEADERS = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.9",
    "Connection":"keep-alive",
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.32.119 Safari/537.36",
    "Cache-Control":"max-age=0, no-cache, no-store",
    "Upgrade-Insecure-Requests":"1"
}

main_url = 'https://www.diamondleague.com/lists-results/statistics/'

class Extract:

    def init_folders(split_csv_name, concat_csv_name):
        if os.path.isdir(split_csv_name):
            pass
        else:
            os.mkdir(split_csv_name)

        if os.path.isdir(concat_csv_name):
            pass
        else:
            os.mkdir(concat_csv_name)

        return split_csv_name, concat_csv_name


    def parse_html(url, soup):
        result = soup.find_all('td', class_='right result')
        wind = soup.find_all('td', class_='right wind')
        # pa_pr_rec = soup.find_all('td', class_='center')
        # pr = soup.find_all('td', class_='center')
        athlete = soup.find_all('td', class_='left achiever')
        birth = soup.find_all('td', class_='center birthdate')
        nat = soup.find_all('td', class_='center nationality')
        race = soup.find_all('td', class_='right')
        place = soup.find_all('td', class_='center place')
        venue = soup.find_all('td', class_='venue')
        date = soup.find_all('td', class_='date')
        rs = soup.find_all('td', class_='center score')

        result_list = [element.text for element in result]
        wind_list = [element.text for element in wind]
        athlete_list = [element.text for element in athlete]
        birth_list = [element.text for element in birth]
        nat_list = [element.text for element in nat]
        full_race_list = [element.text for element in race]
        place_list = [element.text for element in place]
        venue_list = [element.text for element in venue]
        date_list = [element.text for element in date]
        rs_list = [element.text for element in rs]

        race_list = []
        for idx, element in enumerate(full_race_list):
            if idx % 3 == 2:
                race_list.append(element)
            else:
                pass
        return [result_list, wind_list, athlete_list, birth_list, nat_list, race_list, place_list, venue_list, date_list, rs_list]
    

    def partitioned_by_year_to_csv():
        
        years = [year for year in range(2010, date.now().year + 1)]

        for year in years: 
            print(f"Processing {year} data")
            url = f'https://dl.all-athletics.com/dls/en/seasons-list/{year}/ffnnn/10229630/1073741823/detailed'
            response = requests.get(url, headers=HEADERS)
            soup = BeautifulSoup(response.content, 'html.parser')

            data_list = Extract.parse_html(url, soup)
            
            same_length = all(len(lst) == len(data_list[0]) for lst in data_list)

            if same_length:
                print("All lists have the same length.")
            else:
                print("Lists have different lengths.")
                break

            results_df = pd.DataFrame({'results':data_list[0],
                'wind':data_list[1], 
                'athlete':data_list[2],
                'birth_year':data_list[3], 
                'nationality':data_list[4], 
                'race':data_list[5], 
                'place':data_list[6], 
                'venue':data_list[7],
                'date':data_list[8], 
                'rs':data_list[9]})

            today = date.today().strftime('%m%d%Y')
            folder_name = Extract.init_folders('uncleaned_partitioned_output', 'uncleaned_all_years_csv')[0]
            print(f"outputting: uncleaned_partitioned_{year}_{today}.csv")
            results_df.to_csv(f'{folder_name}/uncleaned_partitioned_{year}_{today}.csv')


    def concatenate_partitioned_csv():
        file_paths = sorted(glob(os.path.join('uncleaned_partitioned_output', "*.csv")))
        full_df = (pd.concat([pd.read_csv(input_file_path) for input_file_path in file_paths]))
        today = date.today().strftime('%m%d%Y')
        folder_name = Extract.init_folders('uncleaned_partitioned_output', 'uncleaned_all_years_csv')[1]
        print(f"outputting: uncleaned_all_years_{today}.csv")
        full_df.to_csv(f'{folder_name}/uncleaned_all_years_{today}.csv')


if __name__ == '__main__':
    Extract.init_folders('uncleaned_partitioned_output', 'uncleaned_all_years_csv')
    Extract.partitioned_by_year_to_csv()
    Extract.concatenate_partitioned_csv()