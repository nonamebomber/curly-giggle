import requests
from bs4 import BeautifulSoup
# import lxml


user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
headers = {"User-agent": user}

sessions = requests.Session()
for j in range (1,7):
    # print(f"PAGE - {j}")
    url = f"https://cash-backer.club/shops?page={j}"
    response = sessions.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")
        companies = soup.find_all("div", class_="col-lg-2 col-md-3 shop-list-card pseudo-link no-link")



    for prod in companies:
        if prod.find('div', class_="card mb-4"):
            cashbacks = prod.find('div', class_="card-body")
            cashbacks_prod = cashbacks.text
            with open("cashback.txt", "a", encoding="utf-8") as file:
                file.write(f"{cashbacks_prod}\n")
            # print(cashbacks.text)


# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, "lxml")
#     companies = soup.find_all("div", class_="col-lg-2 col-md-3 shop-list-card pseudo-link no-link")
#     # print(len(companies))
#
#
# for prod in companies:
#     if prod.find('div', class_="card mb-4"):
#         cashbacks = prod.find('div', class_="card-body")
#         # cashbacks_prod = cashbacks.text
#         # with open("cashback.txt", "a", encoding="utf-8") as file:
#         #     file.write(f"{cashbacks_prod}\n")
#         print(cashbacks.text)

