# WEB
from bs4 import BeautifulSoup
import requests

# DOWNLOAD
from pathlib import Path
import shutil

# APP
from constants import *
from photo import *

UNDOWNLOADED_ARTICLES = []

def find_id(doc):
  id_tag = doc.find('div', id='pageTitle')
  id_content = id_tag.contents[-1]
  id = id_content.split()[-1][:-1]

  return id.strip()

def find_year(doc):
  year_tag = doc.find(text="Cota:").parent.parent
  year_content = year_tag.contents[1]
  year = year_content.split("/")[-1]

  return year.strip()
  
def find_description(doc):
  description_tag = doc.find(text="Conţinut:").parent.parent
  description = description_tag.contents[1]
 
  return description.strip()

def find_place(doc):
  place_tag = doc.find(text="Dată/loc:").parent.parent
  place_content = place_tag.contents[1]
  place = place_content.split(",")[0]

  return place.strip()

def find_photo_url(doc):
  photo_tag = doc.find('img', alt="Descarca imagine hi-res").parent
  photo_path = photo_tag['href']
  photo_url = HOME_URL + photo_path

  return photo_url

def download_photo(photo):
  request_result = requests.get(photo.url, stream=True)

  if request_result.ok:
    year_folder_path = OUTPUT_PATH + '/' + photo.year
    Path(year_folder_path).mkdir(parents=True, exist_ok=True)

    output_photo_path = year_folder_path + '/' + photo.title()[:200] + PHOTO_FILE_EXTENSION
    
    with open(output_photo_path, "wb") as f:
      shutil.copyfileobj(request_result.raw, f)
  else:
    print("     ! Can't download photo !")
    UNDOWNLOADED_ARTICLES.append([photo.title(), photo.url])

def download_article(article_url):
  article_request_result = requests.get(article_url)
  document = BeautifulSoup(article_request_result.text, "html.parser")

  id = find_id(document)
  year = find_year(document)
  description = find_description(document)
  place = find_place(document)
  photo_url = find_photo_url(document)

  photo = Photo(id, year, description, place, photo_url)
  download_photo(photo)
  print("     Downloaded photo: " + photo.title())
  