import sys, requests, webbrowser, bs4

print('Googling...')                        #dispay text while downloading Google page
#Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
response = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]), headers = header)

soup = bs4.BeautifulSoup(response.text, "html.parser")
link_res=soup.find_all('div',{'class':'yuRUbf'})
link_list=[]
for item in link_res:
    link=item.find('a')['href']
    link_list.append(link)
#print(link_list)

numOpen = min(5, len(link_list))
for i in range(numOpen):
    # webbrowser.open('http://google.com' + link_list[i].get('href'))
    webbrowser.open(link_list[i])