import requests

headers = {
    'Host': 'www.amazon.in',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'TE': 'Trailers'
}



from bs4 import BeautifulSoup

ra = requests.get('https://www.amazon.in/s?k=tupperware+container', headers=headers)
print(ra.status_code)   

soup = BeautifulSoup(ra.content, 'lxml')
ops = soup.prettify()

#ops = print(soup.title)
#print(ops)


with open('amazon.html','w',encoding='utf-8') as o:
   o.write(str(ops))


