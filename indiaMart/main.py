import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://www.indiamart.com"

r = requests.get(url)
print(r)
# soup = BeautifulSoup(r.content, 'html.parser')
# print(soup.prettify())