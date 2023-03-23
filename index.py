from bs4 import BeautifulSoup
import requests
import datetime
import time
import smtplib
from selenium import webdriver
from selenium.webdriver.common import keys
import pandas as pd
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/example')
def example_route():
    return 'Example route here!!!'


# Connecting to web

URL = f"https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1"

Headers = ({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
           'Accept-Language': 'en-US, en;q=0..5'})

page = requests.get(URL, headers=Headers)

x = page.content
# print(x)

soup = BeautifulSoup(page.content, "html.parser")
# print(soup1)


# soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
node = []
mode = []
dictionary = {}
nedo=[]
for i in range(0,19):
    dataframe = [f"Item{i}"]
    nedo.append(dataframe)
    
print(nedo)

red=input("Enter The Excel file name in which data will be saved:")

for i in range(0, 19):
    
    links = soup.find_all("a", attrs={
                          'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
    URLin = links[0].get('href')
    URLout = "https://amazon.com" + URLin
    
    # print(node)
    
    node.append(URLout)
    # print(URLout)
    # print(node)
    mode.append(node)
    i=i + 1
print(mode)



for i in range(0,19):
    k=nedo[i]
    o=mode[i]
    dictionary[k]=o
    i=i+1
print(dictionary)
    
data=pd.DataFrame(dictionary)
print(data)

s=data.to_csv(f"C:\\Users\\om\\Desktop\\{red}.csv")
print(s)



# print(title)







