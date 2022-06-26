from bs4 import BeautifulSoup

with open("amazon.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")
    
    
tags = doc.find_all("a-section a-spacing-none a-spacing-top-small s-title-instructions-style")

print(tags)
ra = requests.get('https://www.amazon.in/s?k=tupperware+container', headers=headers)

