import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

URL = "https://www.amazon.com/product_you_want_to_buy"
my_email = "your_email"
password = "your_password"

params = {
    "User-Agent": "http_header_value",
    "Accept-Language": "http_header_value",
    "sec-ch-ua": 'http_header_value',
}

link = requests.get(URL, headers=params)
soup = BeautifulSoup(link.content, "lxml")
price = soup.find(name="span", class_="a-offscreen").text.split("$")[1]
item_name = soup.find(id="productTitle").text.strip()

if float(price) < 250:
    with smtplib.SMTP("your_smtp_address") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="your_email",
                            msg=f"Subject:Amazon Price Alert!!\n\nPrice drop! {item_name} is only ${price}! Buy it now!"
                                f"\n{URL}")
