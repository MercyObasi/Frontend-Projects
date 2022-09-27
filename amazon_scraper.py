# import the libraries 
import requests
from bs4 import BeautifulSoup
import time
import datetime
import smtplib
# connect to the website
url = "https://www.amazon.com/hz/wishlist/ls/WKPQ54FUI4JO/ref=nav_wishlist_lists_1"

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36", 
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
    "Accept-Encoding": "gzip, deflate, br",  
    "Upgrade-Insecure-Requests": "1",
    "Connection": "close",
    "DNT":"1"}

r = requests.get(url, headers= header)
soup1 = BeautifulSoup(r.content, "html.parser")
soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
title1 = soup2.find("h2","a",id={"id":"itemName_ILXGG8RKDJQB"}).get_text()
# title2 = soup2.find(id="itemName_I1EMSJ6MOCXIEE").get_text()
price = soup2.find("data-item-prime-info",{"id":'ILXGG8RKDJQB',"asin":'1950784622'}).get_text()
print(price)
#print(title1)

# creating the dataset with csv and Setting the time
import csv
import datetime
today = datetime.date.today()
title1 = title1.strip()
header = ["Title"]
data = [title1, today]


with open("webscraper_dataset.csv","w", newline="", encoding="UTF8") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)
    
