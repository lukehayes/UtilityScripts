from bs4 import BeautifulSoup
import urllib3
import requests
import os
import sys

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

for img in soup.find_all('img', {'data-src': True}):
    images.append(img.get('data-src').lstrip("//"))


counter = 0
print(len(images))

for i in images:
    print(i)
    r = http.request("GET",i)
    filename = "image-" + str(counter) + ".jpg"
    file = open(filename, "wb")
    file.write(r.data)
    file.close()

    counter = counter + 1

if(counter == len(images)):
    os.system("rm -r img")
    print("Downloaded Images - Creating Directory...")
    os.mkdir("img")
    os.system("mv *.jpg img")
    print("Completed.")

