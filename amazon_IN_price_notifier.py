import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

my_email = "YOUR MAIL"
my_pass = "YOUR TOKEN"

urls = [ENTER THE PRODUCT URL]
prices = [ENTER THE LOWEST PRICE]

header = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0',
    "Accept-Language": "en-US,en;q=0.9"
}

for index, url in enumerate(urls):
    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.content, "lxml")

    price = int(
        soup.find("span", class_="a-price-whole").get_text().replace(",", "").replace(".", ""))
    if price < prices[index]:
        print("Consider buying.")
        message = f"Subject:Amazon Price Alert! \n\n URL={url}\n Previous lowest set price = {prices[index]}\nCurrently available for: {price}"
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_pass)
            connection.sendmail(from_addr=my_email,
                                to_addrs="ENTER TO EMAIL", msg=message)
            connection.close()
    elif price > prices[index]:
        print("Better to wait.")
    else:
        print("No change")
