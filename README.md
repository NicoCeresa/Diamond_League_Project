# Diamond_League_Project

## Project Overview

**File Descriptions**
- `web_scraper_v2.py`: parses html from a different url that contains more data
  - separates output files based on the year of the data
  - outputs a concatenated file of all years combined aswell
- `web_scraper_v1.py`: extracts pdfs from the html of the diamond league site
  - with where I am at in the project this is not very useful but handy if I ever need to extract pdfs again
- `pdf_parser.py`: goes into each pdf and extracts data from the pdf
  - again, not used as I have found a better approach but want to keep it here as it is apart of the journey

**What I Plan On Adding in the Near Future**
- Create a full data pipeline and extract insights from the data
- if its possible I want to add functionality of being able to choose what event you want to look at

**Goal**
- My goal for this project is to build a model that forecasts likelihood of who wins the next race based on their previous performances
