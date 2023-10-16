import requests
import curl_moscow
from bs4 import BeautifulSoup
import json


def product_id(soup):
    """Функция собирает ссылки на все продукты с одной страницы"""
    data_id = []
    prodict_id = soup.find_all("div", {"class": "catalog-2-level-product-card product-card subcategory-or-type__products-item catalog--common offline-prices-sorting--best-level with-prices-drop"})
    for prod_id in prodict_id:
        data_id.append(prod_id.get("data-sku"))
    return data_id


def product_name(soup):
    data_name = []
    names = soup.find_all("span", {"class": "product-card-name__text"})
    for name in names:
        data_name.append(name.text.strip())
    return data_name


def product_link(soup):
    data_link = []
    links = soup.find_all("a", {"class": "product-card-name"})
    for link in links:
        data_link.append(f"https://online.metro-cc.ru{link.get('href')}")
    return data_link


def product_price(soup):
    data_price = []
    prices = (soup.find_all("div", {"class": "product-card-prices__content-prices"}))
    for price in prices:
        if price.find("span", {"class": "product-price nowrap product-card-prices__actual style--catalog-2-level-product-card-major-actual catalog--common offline-prices-sorting--best-level"}):
            prc = price.text.replace("д", "").replace("/бт", "").replace("/шт", "").replace("\xa0", "").strip()
            data_price.append(prc)
        if price.find("span", {
            "class": "product-price nowrap product-card-prices__actual style--catalog-2-level-product-card-major-actual color--red catalog--common offline-prices-sorting--best-level"}):
            prc = price.text.replace("д", "").replace("/бт", "").replace("/шт", "").replace("\xa0", "").replace(" ", "").strip().split()
            data_price.append(prc)
    return data_price


def product_brand(soup):
    data_brand = []
    brands = soup.find_all("a", {"class": "product-card-name"})
    for brand in brands:
        data_brand.append(brand.text.strip().split()[1])
    return data_brand


def run_moscow():
    soup = BeautifulSoup(curl_moscow.response.text, "lxml")
    product_id(soup)
    product_name(soup)
    product_link(soup)
    product_price(soup)
    product_brand(soup)
    save(product_id(soup), product_name(soup), product_link(soup), product_price(soup), product_brand(soup))
    total_page = soup.find_all("a", {"class": 'v-pagination__item catalog-paginate__item'})
    for number in total_page:
        number_of_page = int(number.get("href").split("=")[-1])
        page = f"{curl_moscow.response.url}?page={number_of_page}"
        response = requests.get(
            page,
            cookies=curl_moscow.cookies,
            headers=curl_moscow.headers,
        )
        soup = BeautifulSoup(response.text, "lxml")
        product_id(soup)
        product_name(soup)
        product_link(soup)
        product_price(soup)
        product_brand(soup)
        save(product_id(soup), product_name(soup), product_link(soup), product_price(soup), product_brand(soup))


def save(data_id, data_name, data_link, data_price, data_brand):
    for index, item in enumerate(data_id):
        data = {
            "id продукта": data_id[index],
            "наименование": data_name[index],
            "ссылка на товар": data_link[index],
            "регулярная цена": data_price[index],
            "промо цена": data_price[index],
            "бренд": data_brand[index]
        }

        with open("moscow.json", "a", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
