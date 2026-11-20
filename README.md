# 图书爬虫 books-scraper

从 books.toscrape.com（爬虫练手网站）抓取图书书名和价格，存进 Excel。

## 能抓到什么

- 一共 50 页、1000 本书
- 每本：书名、价格（£）

## 文件说明

- `spider1.py`：第一步，下载一页源码，看状态码
- `spider2.py`：第二步，用 BeautifulSoup 挑出 20 本书的书名和价格，打印出来
- `spider3.py`：第三步，20 本存进 `books.xlsx`
- `spider4.py`：完整版，50 页全抓，存进 `books_all.xlsx`

## 怎么跑

```bash
pip install requests beautifulsoup4 openpyxl
python spider4.py
```

跑完在当前文件夹找 `books_all.xlsx`。50 页大概 1 分钟，每页歇 1 秒。

## 说明

- 目标网站是公开的爬虫练手站，数据是随机生成的，没有真实含义
- 只做学习和作品展示，不爬真实网站，不碰登录和付费内容
