from bs4 import BeautifulSoup
import requests
import datetime
import csv

#city = input("Type Exact: (St.-Petersburg or weston or Deerfield-Beach):")
city = "Sunrise"

url =f'https://www.realtor.com/realestateandhomes-search/{city}_FL/show-recently-sold'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
page = requests.get(url, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")
soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
rees = soup2.find_all('div', class_="card-content")
cur = datetime.date.today()
curf = cur.strftime('%m/%d/%y')
tim = datetime.datetime.now()
tim2 = tim.strftime('%H:%M%p %Z')
fiile = 'C:/Users/Sebastian/Desktop/Portfolio Projects/Cert Projs/Py/RealEstate'
filepath = fiile+"/comp"+'list'+'.csv'
print(filepath)
header = ['Address', 'Address2', 'Price', 'Bed', 'Bath', 'Sqft', 'Date', 'Time']

with open(filepath, 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for a in rees:
      try:
        saddy = a.find("div", {"data-testid": "card-address-1"}).text.strip()
        saddy2 = a.find("div", {"data-testid": "card-address-2"}).text.strip()
        sprice = a.find("div", {"data-testid": "card-price"}).text.strip().replace(",","").replace("$","")
        sbed = a.find("li", {"data-testid": "property-meta-beds"}).text.strip()[:1]
        sbath = a.find("li", {"data-testid": "property-meta-baths"}).text.strip()[:1]
        ssqft = a.find("li", {"data-testid": "property-meta-sqft"}).text.strip()[:5].replace(",","")
        data = [saddy, saddy2, sprice, sbed, sbath, ssqft, curf, tim2]

        writer.writerow(data)
        print(saddy, saddy2, sprice, sbed, sbath, ssqft, curf, tim2)
      except Exception as e:
        print('0')