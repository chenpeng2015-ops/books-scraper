import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

url = 'http://books.toscrape.com/'
resp = requests.get(url)
resp.encoding = resp.apparent_encoding
soup = BeautifulSoup(resp.text, 'html.parser')
books = soup.find_all('article', class_='product_pod')

wb = Workbook()
ws = wb.active
ws['A1'] = '书名'
ws['B1'] = '价格'

r = 2
for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    ws[f'A{r}'] = title
    ws[f'B{r}'] = price
    r += 1

wb.save('books.xlsx')
print('存好了，一共', len(books), '本')
