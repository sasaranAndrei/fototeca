# APP
from constants import *
from article import *

def find_articles(document):
  desc_class_divs = document.find_all("div", class_="descr")
  articles = []

  for div in desc_class_divs:
    articles.append(div.contents[0]['href'])

  articles = map(lambda x: HOME_URL + x, articles)

  return articles

def download_images_from_page(document):
  articles = find_articles(document)

  for article in articles:
    download_article(article)

def find_next_page_url(document):
  next_page_tag = document.find('img', alt="pagina urmatoare >").parent
  next_page_path = next_page_tag['href']
  next_page_url = ARCHIVE_MAIN_PAGE_URL + next_page_path

  return next_page_url
