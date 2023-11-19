
# 1 ЗАДАНИЕ но я не разобралась как поместить все товары в excel


import requests
from bs4 import BeautifulSoup
import openpyxl

url = "https://allo.ua/ua/products/notebooks/dir-desc/order-review/"
user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
headers = {"user-agent": user}

sessions = requests.Session()

for j in range(1, 25):
    url = "https://allo.ua/ua/products/notebooks/dir-desc/order-review/p-3/"
    response = sessions.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")

        products = soup.find_all("div", class_="product-card")

        for prod in products:
            if prod.find('div', class_="v-pb__old"):
                price = prod.find("div", class_="v-pb__old")
                title = prod.find("a", class_="product-card__title")
                review = prod.find("span", class_="review-button__text review-button__text--count")
                price_prod = price.text
                title_prod = title.text
                review_prod = review.text

                book = openpyxl.Workbook()
                sheet = book.active
                sheet["A1"] = "product title"
                sheet["B1"] = "price"
                sheet["C1"] = "reviews"

                sheet[f"A{1}"] = title_prod
                sheet[f"B{1}"] = price_prod
                sheet[f"C{1}"] = review_prod

                book.save("catalog.xlsx")

                book.close


                with open("catalog.txt", "a", encoding="utf-8") as file:
                    file.write(f"{price_prod} {title_prod} {review_prod}\n")



# 2 ЗАДАНИЕ

import requests
from bs4 import BeautifulSoup
import openpyxl

url = "https://allo.ua/ua/products/notebooks/dir-desc/order-review/"
user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
headers = {"user-agent": user}

sessions = requests.Session()

for j in range(1, 25):
    url = "https://allo.ua/ua/products/notebooks/dir-desc/order-review/p-3/"
    response = sessions.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")

        products = soup.find_all("div", class_="product-card")

        for prod in products:
            if prod.find('div', class_="v-pb__old"):
                price = prod.find("div", class_="v-pb__cur discount")
                title = prod.find("a", class_="product-card__title")
                review = prod.find("span", class_="review-button__text review-button__text--count")
                price_prod = price.text
                title_prod = title.text
                review_prod = review.text

                book = openpyxl.Workbook()
                sheet = book.active
                sheet["A1"] = "product title"
                sheet["B1"] = "price"
                sheet["C1"] = "reviews"

                sheet[f"A{1}"] = title_prod
                sheet[f"B{1}"] = price_prod
                sheet[f"C{1}"] = review_prod

                book.save("catalog.xlsx")

                book.close

                with open("catalog.txt", "a", encoding="utf-8") as file:
                    file.write(f"{price_prod} {title_prod} {review_prod}\n")
