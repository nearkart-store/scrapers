import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://amazon.in"

r = requests.get(url)
print(r)
# soup = BeautifulSoup(r.content, 'html.parser')
# print(soup.prettify())