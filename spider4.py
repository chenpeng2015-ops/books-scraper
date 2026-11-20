import time
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws['A1'] = '书名'
ws['B1'] = '价格'

r = 2
for p in range(1, 51):
    url = f'http://books.toscrape.com/catalogue/page-{p}.html'
    resp = requests.get(url)
    resp.encoding = resp.apparent_encoding
    soup = BeautifulSoup(resp.text, 'html.parser')
    books = soup.find_all('article', class_='product_pod')
    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        ws[f'A{r}'] = title
        ws[f'B{r}'] = price
        r += 1
    print('第', p, '页抓完，一共', r - 2, '本')
    time.sleep(1)

wb.save('books_all.xlsx')
print('全抓完了，一共', r - 2, '本')
