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


testa = tree.xpath('//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[50]/div/div/div/div/div[2]/div[1]/h2/a/span[1]')
print(testa[0].text)

prica = tree.xpath('//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[50]/div/div/div/div/div[2]/div[3]/div/a/span[1]/span[2]/span[2]')
print(prica[0].text)