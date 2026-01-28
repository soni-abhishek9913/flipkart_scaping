#author:=soni abhishek 

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
driver.get("https://www.flipkart.com/")

time.sleep(1)
all_data = []

for page in range(1, 11):
    print(f"Scraping page {page}")

    url = f"https://www.flipkart.com/search?q=mobile+under+50000&page={page}"
    driver.get(url)
    time.sleep(4)

    soup = BeautifulSoup(driver.page_source, "lxml")
    products = soup.find_all("div", class_="jIjQ8S")

    print("Products found:", len(products))

    for p in products:
        name = p.find("div", class_="RG5Slk")
        price = p.find("div", class_="hZ3P6w DeU9vF")
        rating = p.find("div", class_="MKiFS6")
        desc = p.find("div", class_="CMXw7N")

        if name and price:
            all_data.append([
                name.text.strip(),
                price.text.strip(),
                rating.text.strip() if rating else "No Rating",
                desc.text.strip() if desc else "No Description"
            ])

driver.quit()

df = pd.DataFrame(all_data, columns=["Name", "Price", "Rating", "Description"])
df.to_csv("flipkart_all_pages.csv", index=False, encoding="utf-8")


