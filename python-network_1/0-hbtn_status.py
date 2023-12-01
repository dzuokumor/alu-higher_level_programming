#!/usr/bin/python3
"""Fetches https://alu-intranet.hbtn.io/status."""
import urllib.request

def get_url_content(url):
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode()

        print(body)

    except urllib.error.URLError as e:
        print(f"Failed to reach the server: {e.reason}")

if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    get_url_content(url)
