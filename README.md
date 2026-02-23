# File-Enumeration

# PDF Date Fetcher

A simple Python script that iterates over a date range and attempts to download PDF files from a server using a date-based filename pattern.

## Requirements

- Python 3.6+
- `requests` library

Install the required dependency:

pip install requests

## Configuration

Before running the script, update the following variables inside the file:

base_url = "http://192.168.1.1/.../"
file_suffix = "-upload.pdf"                  
start_date = datetime(2020, 1, 1)            
end_date = datetime(2020, 12, 31)           

```base_url``` → Set the target server and directory.

```file_suffix``` → Change if the filename pattern is different.

```start_date / end_date``` → Define the date range to scan.

## Usage

Run the script with:

```python script.py```

All files returning HTTP 200 will be saved in the current directory.
