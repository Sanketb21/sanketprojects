import requests, os, bs4

url = 'http://xkcd.com'                         #starting url
os.makedirs('xkcd', exist_ok= True)             #stores comics in ./xkcd
while not url.endswith('#'):
    print("Downloading page %s..."%url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)
    comicEle = soup.select('#comic img')
    if comicEle == []:
        print("Could not find Comic Image")
    else:
        comicUrl = 'http:' + comicEle[0].get('src')

        print("Downloading image %s..." %(comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()

        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')
print('Done')