import requests
from bs4 import BeautifulSoup as bs

url = "https://github.com/settings/profile"
r = requests.get(url)
soup = bs(r.content, "html.parser")
res = soup.title
print(res.get_text())

github_name = input("Enter username:")
url = "https://github.com/"+github_name
r = requests.get(url)
soup = bs(r.content, "html.parser")
image = soup.find("img", {"alt": "@MercyObasi"})["src"]
print(image)