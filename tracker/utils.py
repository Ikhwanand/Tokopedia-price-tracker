import requests
from bs4 import BeautifulSoup
import lxml
import re


# url = "https://www.tokopedia.com/cockomputer/msi-b650m-gaming-wifi-am5-1730759306947102219?source=homepage.top_carousel.0.38456"

def get_link_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
        "Accept-Language": "en"
    }

    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text, 'lxml')

    name = soup.select_one(selector="h1.css-1xfedof").get_text()
    image_url = soup.select_one(selector="img.css-1c345mg").get('src')

    price = soup.select_one(selector="div.price").get_text()
    formated_price = re.sub(r'^Rp\s*', '', price)

    return name, formated_price, image_url


