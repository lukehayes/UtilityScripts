from bs4 import BeautifulSoup
import urllib3
import requests

# response = requests.get("http://imgsrc.ru/wizarden/68739106.html?pwd=&per_page=12")

http = urllib3.PoolManager()
url = "http://imgsrc.ru/main/tape.php?aid=2326551&pwd="
r = http.request("GET",url)

soup = BeautifulSoup(r.data, 'html.parser')




images = []


for img in soup.find_all('img', {'data-src': True}):
    images.append(img.get('data-src').lstrip("//"))



counter = 0

for i in images:
    print(i)
    r = http.request("GET",i)
    filename = "image-" + str(counter) + ".jpg"
    file = open(filename, "wb")
    file.write(r.data)
    file.close()

    counter = counter + 1

if(counter == len(images)):
    os.mkdir("images", "755")
    os.system("mv *.jpg images")

