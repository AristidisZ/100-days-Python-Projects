import requests

from bs4 import BeautifulSoup
import lxml
my_price = 1800
url = 'https://www.amazon.com/ASUS-ROG-Strix-Gaming-Laptop/dp/B0BV7XQ9V9?ref_=Oct_DLandingS_D_cd7fb716_0&th=1'

headers = {

    "Accept-Language": "en-US,en;q=0.9"

}
responce = requests.get(url=url, headers=headers)
data = responce.text

soup = BeautifulSoup(data, 'html.parser')

# print(soup.prettify())

price = soup.find_all(class_="a-offscreen")[1].getText().replace("$","").replace("," , "")
print(float(price))

if float(price) <= my_price:
    print("sent email")