# File-Enumeration

PDF Date Scraper

Simple Python script that iterates over a date range and attempts to download PDF files from a server using a date-based filename pattern.

Requirements

Python 3.6+

requests library

Install dependency:

pip install requests
Configuration

Before running the script, adjust the following variables:

base_url = "http://10.10.10.248/documents/"   # Target base URL
file_suffix = "-upload.pdf"                  # File name suffix
start_date = datetime(2020, 1, 1)            # Start date
end_date = datetime(2020, 12, 31)            # End date

base_url → Set the target server and directory.

file_suffix → Modify if the file naming pattern differs.

start_date / end_date → Define the date range to scan.

Usage
python script.py

Files found (HTTP 200) will be saved in the current directory.
