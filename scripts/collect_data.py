import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com"
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")
quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

data = []

for q, a in zip(quotes, authors):
    data.append([q.text, a.text])

df = pd.DataFrame(data, columns=["quote", "author"])
df.to_csv("datasets/quotes.csv", index=False)


print("Data collected and saved as quotes.csv!")
