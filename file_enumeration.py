#!/usr/bin/env python3

import requests
from datetime import datetime, timedelta

base_url = "http://192.168.1.1/..."
file_suffix = "-upload.pdf"

start_date = datetime(2020, 1, 1)
end_date = datetime(2020, 12, 31)

current_date = start_date
while current_date <= end_date:
    date_str = current_date.strftime("%Y-%m-%d")
    url = f"{base_url}{date_str}{file_suffix}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"[+] Found: {url}")
            with open(f"{date_str}{file_suffix}", "wb") as f:
                f.write(response.content)
        elif response.status_code != 404:
            print(f"[?] Unexpected status ({response.status_code}) at: {url}")
    except requests.RequestException as e:
        print(f"[-] Error fetching {url}: {e}")
    current_date += timedelta(days=1)
