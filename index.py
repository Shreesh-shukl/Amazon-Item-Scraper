from bs4 import BeautifulSoup
import requests
import datetime
import time
import smtplib

#Connecting to web
for i in range(1,10):
    i+=1
URL=f"https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_{i}"

headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")
print(soup1)

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find(id='anonCarousel1').get_text()

print(title)