import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv

# 123

url = "https://www.777555.by/kompyutery_i_seti/kompyutery_i_komplektuyuschie/ssd/"


def get_html(url):
    response = requests.get(url)
    return response.text

def write_csv(data):
    with open("data.csv", "a") as file:
        writer = csv.writer(file)

        writer.writerow((data["title"],data["price"],data["link"]))

def get_links(html):
    soup = BeautifulSoup(html,"lxml")
    catalog = soup.find_all("div", class_="catalog-item")
    print(type(catalog))
    #print(catalog)


    for item in catalog:
        link = item.find("div", class_="catalog-item-title").find("a").get("href")
        title = item.find("div", class_="catalog-item-title").find("a").text
        price = item.find("div", class_="catalog-item-price").text
        # print("title = " + str(title))
        # print("price = " + str(price))
        # print("link = " + str(link))
        data = {"link": link, "title": title, "price":price}


        write_csv(data)


html = get_html(url)
get_links(html)
print("DONE")


