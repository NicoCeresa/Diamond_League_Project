import os
import boto3
from glob import glob
from hush import aws_creds
from web_scraper_v2 import Extract

s3 = boto3.resource(
    service_name = 's3',
    region_name = 'us-west-1',
    aws_access_key_id = aws_creds['AWS_access_key'], # create a separate file to store this sensitive info
    aws_secret_access_key=aws_creds['AWS_secret'] # ^^^
)

class Load_S3:
    
    def load_partitioned_csv():
        partitioned_folder = "uncleaned_partitioned_output"
        partitioned_csvs = sorted(glob(os.path.join(partitioned_folder, '*.csv')))

        for csv in partitioned_csvs:
            # Filename is what your csv is named locally
            # Key is what it will be named in the s3
            s3.Bucket('diamond-league-project-s3').upload_file(Filename=csv, Key=csv)
    
            
    def load_full_csv():
        all_years_folder = "uncleaned_all_years_csv"
        full_csv = os.path.join(all_years_folder, 'uncleaned_all_years.csv')
        s3.Bucket('diamond-league-project-s3').upload_file(Filename=full_csv, Key=full_csv)
        

if __name__ == '__main__':
    Load_S3.load_partitioned_csv()
    Load_S3.load_full_csv()