import requests
from bs4 import BeautifulSoup
import pandas as pd
import xlsxwriter
import os




def generate_url_address(text: str, pages: int):
    text = text.strip().replace(" ", "+")
    responses = []
    
    for page in range(1, pages+1):
        url = f"https://www.ebay.com/sch/i.html?_from=R40&_nkw={text}&_sacat=0&_pgn={page}"
        response = requests.get(url)
        responses.append(response.content)
    
    return responses


def parse(data_list): 
    products_list = []

    for data in data_list:
        soup = BeautifulSoup(data, "lxml")
        block = soup.find_all('div', class_="s-item__wrapper clearfix")
        
        for item in block:
            link = item.find(
                'a', class_="s-item__link").get("href")
            title = item.find(
                'div', class_="s-item__title").find("span", role="heading").get_text(strip=True)
            subtitle = item.find(
                'div', class_="s-item__subtitle").get_text(strip=True) if item.find('div', class_="s-item__subtitle") else None
            price = item.find(
                'div', class_="s-item__detail s-item__detail--primary").find('span', class_="s-item__price").get_text(strip=True)
            image = item.find(
                'div', class_="s-item__image-wrapper image-treatment").find("img")['src']

            products = {
                'link': link,
                'title': title,
                'subtitle': subtitle,
                'price': price,
                'image': image,
            }
            products_list.append(products)

    return products_list[2:]


def scrape_ebay(text: str, total_pages: int):
    responses = generate_url_address(text, total_pages)
    products = parse(responses)
    return products


def save_to_excel(products, filename):
    ebay_data = pd.DataFrame(products)
    
    with pd.ExcelWriter(filename, engine='xlsxwriter') as writer:
        ebay_data.to_excel(writer, index=False, sheet_name='Sheet1')



products = scrape_ebay(text=input("Enter a product: "), total_pages=2)
filename = 'ebay_products.xlsx'
save_to_excel(products, filename)