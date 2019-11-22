import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv

# csv:  price , BYN , / , units , currency abbreviation (exmpl:  2,0479 BYN / 1 USD)

url = "https://myfin.by/bank/kursy_valjut_nbrb"
headers = {"accept": "*/*", "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}

def get_html(url, headers):
    session = requests.Session()
    request = session.get(url, headers=headers)
    if request.status_code == 200:
        print("Status code = 200")
    else:
        print("NO CONNECTION")
    return request.text

def write_csv(data):
    with open("data.csv", "a") as file:
        writer = csv.writer(file)
        str = f"{data['price']} BYN / {data['units']} {data['curr_abbr']}"
        writer.writerow([str])

def get_links(html):
    soup = BeautifulSoup(html,"lxml")
    trs = soup.find("table", class_="rates-table-nbrb").find("tbody", class_="table-body").find_all("tr")


    for tr in trs:
        price = tr.find("td", class_="course").text
        units = tr.find("td", class_="code").text
        curr_abbr = tr.find_all("td")[3].text

        data = {"price":price, "units":units, "curr_abbr":curr_abbr}

        write_csv(data)

print("START")
html = get_html(url, headers)
get_links(html)
print("Dev01 END")


