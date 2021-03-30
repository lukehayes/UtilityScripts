#!/usr/bin/env python3

# -------------------------------------------------------------
# A simple image scraping script for bulk downloading of images.
# -------------------------------------------------------------
from bs4 import BeautifulSoup
import urllib3
import requests
import os, sys, re

http = urllib3.PoolManager()
count = sys.argv[1]
url = sys.argv[2]

global images
images = []

global filenames
filenames = []

def ClearLists():
    images.clear()
    print("Image List Cleared")
    filenames.clear()
    print("Filenames List Cleared")

def MoveImages():
    print("Moving Downloaded Images...")
    os.system("mv *.jpg Images")
    print("Move Completed.")


def GetPageData(url):
    """ Send Request and Init Beautiful Soup """
    r = http.request("GET", str(url))
    soup = BeautifulSoup(r.data, 'html.parser',  from_encoding="iso-8859-1")
    return soup

def FindImages(url):
    soup = GetPageData(url)
    print("Images")

    for img in soup.find_all('img', {'data-src': True}):
        images.append(img.get('data-src').lstrip("//"))
        print(img)

def PrepareImageURLS():
    pattern = "imgsrc.ru_[0-9A-Za-z]+\.jpg"

    for url in images:
        match = re.search(pattern, url)

        if match:
            filenames.append(match.group(0))

def WriteImages():
    for i in range(0, len(images)):
        r = http.request("GET", images[i])
        file = open(filenames[i], "wb")
        print("Writing " + filenames[i])
        file.write(r.data)
        file.close()
    print("Image Writing Finished.")


def IteratePages(url, n):
    for x in range(0,n,12):
        print("Starting Round " + str(x))
        if x > 0:
            before = "=" + str(x - 12) + "&"
            after = "=" + str(x) + "&"
        else:
            before=""
            after=""
        url = url.replace(before, after)
        print("Trying URL: " + url)

        FindImages(url)
        PrepareImageURLS()

        print("Images: " + str(len(images)))
        print("Filenames: " + str(len(filenames)))
        # WriteImages()
        # MoveImages()
        # print("Finished Round " + str(x))
        # ClearLists()

IteratePages(url, int(count))

WriteImages()
MoveImages()
# ClearLists()





