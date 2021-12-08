# CORE
from bs4 import BeautifulSoup
import requests
from requests.api import request
import shutil
from photo import Photo

# APP
from constants import *
from main import *

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
    output_photo_path = OUTPUT_PATH + '/' + photo.title() + PHOTO_FILE_EXTENSION
    
    with open(output_photo_path, "wb") as f:
      shutil.copyfileobj(request_result.raw, f)
  else:
    print("Can t download photo")

def test_requests_bs4():
  # TEST_URL = "https://fototeca.iiccmer.ro/picdetails.php?picid=30656X1X5732"
  # TEST_URL = "https://fototeca.iiccmer.ro/picdetails.php?picid=30704X12X5732"
  # TEST_URL = "https://fototeca.iiccmer.ro/picdetails.php?picid=30980X70X5732"
  # TEST_URL = "https://fototeca.iiccmer.ro/picdetails.php?picid=30764X23X5732"
  # TEST_URL = "https://fototeca.iiccmer.ro/picdetails.php?picid=31786X277X5732"
  # TEST_URL = "https://fototeca.iiccmer.ro/picdetails.php?picid=32282X422X5732"
  TEST_URL = 'https://fototeca.iiccmer.ro/picdetails.php?picid=38004X2672X5732'

  download_article(TEST_URL)

if __name__ == '__main__':
  test_requests_bs4()
