#!/usr/bin/env python3

from bs4 import BeautifulSoup
import urllib3
import requests
import os, sys, re

# response = requests.get("http://imgsrc.ru/wizarden/68739106.html?pwd=&per_page=12")

http = urllib3.PoolManager()

try:
    url = sys.argv[1]
    r = http.request("GET", str(url))
    soup = BeautifulSoup(r.data, 'html.parser')
except IndexError as e:
    print("Missing a url to search.")
    print("Exiting...")
    sys.exit()

images = []
filenames = []

for img in soup.find_all('img', {'data-src': True}):
    images.append(img.get('data-src').lstrip("//"))

pattern = "imgsrc.ru_[0-9A-Za-z]+\.jpg"

for url in images:
    match = re.search(pattern, url)
    filenames.append(match.group(0))

for i in range(0, len(images)):
    r = http.request("GET", images[i])
    file = open(filenames[i], "wb")
    print("Writing " + filenames[i])
    file.write(r.data)
    file.close()

print("Downloaded Images - Creating Directory...")
os.system("mv *.jpg img")
print("Completed.")

