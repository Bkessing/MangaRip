import requests
from bs4 import BeautifulSoup
import urllib.request
import os
import time


def getlink(url):
    r = requests.get(url)
    result = r.content
    soup = BeautifulSoup(result, 'html.parser')
    hold = soup.find_all('img', {"id": "img"})
    hold2 = soup.find_all('div', {"id": 'imgholder'})
    if (hold==[] or hold2==[]):
        return 0
    else:
        hold2 = hold2[0].find_all('a')
        ref = hold2[0].get('href')
        mangaName = str(ref)
        link = hold[0].get('src')
        send = [link, mangaName]
        return send


def download(link):
    home = os.path.expanduser("~")
    path = home + '\Desktop'+ '/' + mangaName
    if not os.path.exists(path):
        os.makedirs(path)
    img_data = requests.get(link).content
    picname =chapter.replace("/","_")
    with open(path + '/' + picname[1:] +'.jpg', 'wb') as handler:
        handler.write(img_data)



mangaName = input("Enter manga name: ")
mangaName = mangaName.lower()
mangaName = mangaName.strip()
mangaName = mangaName.replace(" ","-")

start = input("Enter starting chapter: ")


chapter = "/" + mangaName+"/"+start
masterurl = 'https://www.mangareader.net'
url = masterurl + chapter
page = 0
count = 0

while(1):
    link = getlink(url)
    if (link == 0):
        break
    download(link[0])
    os.system('cls')
    print('Downloaded ' + chapter[1:])
    chapter = link[1]
    page = page +1
    url = masterurl + link[1]
    count = count + 1

if(count == 0):
    print("No manga found")
    time.sleep(3)
else:
    print("Files Downloaded")
    time.sleep(3)

