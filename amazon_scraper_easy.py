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

from lxml import html

page = requests.get('https://www.amazon.in/s?k=tupperware+container', headers=headers)

tree = html.fromstring(page.content)

namu = tree.xpath('//div[@class="a-section a-spacing-none a-spacing-top-small s-title-instructions-style"]/h2/a/span')


x = 0

while(x < len(namu)):
    print("Name : " + namu[x].text + "\n")
    x = x + 1

    
