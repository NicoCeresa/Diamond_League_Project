import boto3
from web_scraper_v2 import Extract

all_years = Extract.concatenate_partitioned_csv()
partitioned = Extract.partitioned_by_year_to_csv()
