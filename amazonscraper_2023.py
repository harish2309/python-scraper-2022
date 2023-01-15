import requests
from bs4 import BeautifulSoup
url = "https://www.amazon.in/s"
querystring = {"":"","k":"xcluma"}
payload = ""
headers = {"cookie": "session-id=259-0872436-7583763; session-id-time=2082758401l; i18n-prefs=INR; ubid-acbin=257-5294678-5626453; session-token=Ti90EwhUXpo9GKig+1i3yVwvDn0rA8j6HV9dZPCVkkXeqK2LYsKHIDiHcxHjO9uffnThJ3b8KWkzYOuDE7zbiN86gIq9JQOBE3DopRlyfz1/IiYpxXyOUqY/0yf33QIXSS+4Lqw64ku23uDzM3KC+fsmg3ahnaVfRlSpVoet3XCGooTatDV2nLqXdsZt9qe1PHKt7ywLOfDF1Ix3S1EZC3mHTFOyDh+i4bWLs7ePape23wTJiJEpLw=="}
           
response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
#print(response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')

release = soup.find_all('div',class_='a-section a-spacing-small puis-padding-left-small puis-padding-right-small')

for amaz in release:
    prodname = amaz.find('span', {'class' : 'a-size-base-plus a-color-base a-text-normal'})
    prices = amaz.find('span', {'class' : 'a-price-whole'})
    print(prodname.text)
    print(prices.text)

