# Diamond_League_Project

## How To Run
run the file `web_scraper_v2.py` like this:
`python3 web_scraper_v2.py` in your terminal
- You can use my aws_connect.py file as a guidline of how to connect and upload to your s3 bucket

**Expected Output**
- The script should output two folders:
  1) a folder that contains the partitioned by year CSVs
  2) a folder that contains a CSV created from concatenating the partitioned CSVs 

## Project Overview

**File Descriptions**
- `web_scraper_v2.py`: parses html from a different url that contains more data
  - separates output files based on the year of the data
  - outputs a concatenated file of all years combined aswell
- `load_to_s3.py`: connects to my s3 Bucket and uploads csvs to the bucket
- `web_scraper_v1.py`: extracts pdfs from the html of the diamond league site
  - with where I am at in the project this is not very useful but handy if I ever need to extract pdfs again
- `pdf_parser.py`: goes into each pdf and extracts data from the pdf
  - again, not used as I have found a better approach but want to keep it here as it is apart of the journey

**Next Steps**
- Add location data such as:
  - Elevation, temperature, and weather
- Try to find speed tracking data
- Create Visualizations/Dashboard
- Add a transform file
  - add 19 or 20 to birth year
    - add age
  - make DOB more date-like
  - add date of event col
    - add weather data for the date
  - make col for venue location
    - remove the location from og venue col
  - add race distance
  
- load to a mysql db (dbeaver maybe)
- orchestrate with airflow on an ec2 container
- Create a full data pipeline
- Use regression to predict their next race
- if its possible I want to add functionality of being able to choose what event you want to look at

**Metrics to track**
- How much people are affected by different weathers
- Are any tracks "faster" than others

**Goal**
- My goal for this project is to build a model that forecasts likelihood of who wins the next race based on their previous performances
