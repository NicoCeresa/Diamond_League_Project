import os
import boto3
import requests
import numpy as np
import pandas as pd
from glob import glob
from bs4 import BeautifulSoup
from hush import aws_creds, HEADERS
from datetime import datetime as date

"""
main_url = 'https://www.diamondleague.com/lists-results/statistics/'
"""

class Extract:

    def init_folders(split_folder_name, concat_folder_name):
        """
        - Checks if the desired folders exist
        - If they do not it creates them

        Args:
            split_csv_name (_type_): Name of folder for split csvs
            concat_csv_name (_type_): Name of folder for concatenated csv

        Returns:
            Names of the folders for later use
        """
        if os.path.isdir(split_folder_name):
            pass
        else:
            os.mkdir(split_folder_name)

        if os.path.isdir(concat_folder_name):
            pass
        else:
            os.mkdir(concat_folder_name)

        return split_folder_name, concat_folder_name
    
    
    def same_length(data_list: list):
        """_summary_
        check for if the lists in a list of lists are all equal
        Args:
            data_list (list): a list of lists
        """
        same_length = all(len(lst) == len(data_list[0]) for lst in data_list)
        if same_length:
            print("All lists have the same length.")
        else:
            print("Lists have different lengths.")


    def extract_data(soup, class_name):
        elements = soup.find_all('td', class_=class_name)
        return [element.text for element in elements]

    def parse_html(url, soup):
        """
        Grabs the html using Beautiful soup and gets the text
        Args:
            url (str): url of what you want to scrape
            soup (Beautifulsoup): Initialization of Beautifulsoup

        Returns:
            _type_: _description_
        """
        
        result_list = Extract.extract_data(soup, 'right result')
        wind_list = Extract.extract_data(soup, 'right wind')
        athlete_list = Extract.extract_data(soup, 'left achiever')
        birth_list = Extract.extract_data(soup, 'center birthdate')
        nat_list = Extract.extract_data(soup, 'center nationality')
        full_race_list = Extract.extract_data(soup, 'right')
        place_list = Extract.extract_data(soup, 'center place')
        venue_list = Extract.extract_data(soup, 'venue')
        date_list = Extract.extract_data(soup, 'date')
        rs_list = Extract.extract_data(soup, 'center score')


        race_list = []
        for idx, element in enumerate(full_race_list):
            if idx % 3 == 2:
                race_list.append(element)
            else:
                pass
        return [result_list, wind_list, athlete_list, birth_list, nat_list, race_list, place_list, venue_list, date_list, rs_list]
        

    def partitioned_by_year_to_csv():
        """
        Input: nothing
        Returns:
            Dictionary: A dictionary containing the dataframes where the key 
            is the year and the value is the dataframe
        """
        df_dict = {}
        years = [year for year in range(2010, date.now().year + 1)]

        for year in years: 
            print(f"Processing {year} data")
            url = f'https://dl.all-athletics.com/dls/en/seasons-list/{year}/ffnnn/10229630/1073741823/detailed'
            response = requests.get(url, headers=HEADERS)
            soup = BeautifulSoup(response.content, 'html.parser')
            data_list = Extract.parse_html(url, soup)
            Extract.same_length(data_list=data_list)

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

            folder_name = Extract.init_folders('uncleaned_partitioned_output', 'uncleaned_all_years_csv')[0]
            results_df.to_csv(f'{folder_name}/uncleaned_partitioned_{year}.csv', index=False)
            df_dict[f"{year}"] = results_df
        return df_dict

        
    def concatenate_partitioned_csv():
        file_paths = sorted(glob(os.path.join('uncleaned_partitioned_output', "*.csv")))
        full_df = (pd.concat([pd.read_csv(input_file_path) for input_file_path in file_paths]))
        folder_name = Extract.init_folders('uncleaned_partitioned_output', 'uncleaned_all_years_csv')[1]
        return full_df
        

if __name__ == '__main__':
    Extract.init_folders('uncleaned_partitioned_output', 'uncleaned_all_years_csv')
    Extract.partitioned_by_year_to_csv()
    Extract.concatenate_partitioned_csv()