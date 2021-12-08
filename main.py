# CORE
import sys
import getopt

# WEB
from bs4 import BeautifulSoup
import requests
 
# APP
from constants import *
from page import *
from article import *
from photo import *

def find_max_page_number():
  archive_main_page_request = requests.get(ARCHIVE_MAIN_PAGE_URL)
  document = BeautifulSoup(archive_main_page_request.text, "html.parser")

  max_page_tag = document.find(id="searchdetails")
  max_page = int(max_page_tag.contents[0].split(' ')[-1])

  return max_page

def download_data():
  page_step = 0
  next_page_url = ARCHIVE_MAIN_PAGE_URL

  while (page_step < PAGE_STEP_MAX):
    current_page_request_result = requests.get(next_page_url)
    document = BeautifulSoup(current_page_request_result.text, "html.parser")
    
    print("   Page " + str(page_step + 1) + "/" + str(PAGE_STEP_MAX))
    download_images_from_page(document)
    
    if page_step != PAGE_STEP_MAX - 1:
      next_page_url = find_next_page_url(document)
    page_step += 1

def download_data_from_page(page):
  page_step = 0
  next_page_url = ARCHIVE_MAIN_PAGE_URL
  
  while (page_step < page - 1):
    current_page_request_result = requests.get(next_page_url)
    document = BeautifulSoup(current_page_request_result.text, "html.parser")

    next_page_url = find_next_page_url(document)
    page_step += 1

  target_page_request_result = requests.get(next_page_url)
  document = BeautifulSoup(target_page_request_result.text, "html.parser")

  print("   Page " + str(page))
  download_images_from_page(document)

def print_help():
  print("usage: ./fototeca [option] [arg]")
  print("Options and arguments:")
  print("-h           : print this help message, also --help")
  print("-s <number>  : download the photos from the first <number> pages, also --step")
  print("-p <number>  : download the photos from the page <number>, also --page")
  print()
  print("If you don't provide any options and arguments, the script will download all images from: https://fototeca.iiccmer.ro/fototeca/")
  print()
  print("Example: ./fototeca -s 3")
  print("Example: ./fototeca --step 3")
  print("Example: ./fototeca -p 42")
  print("Example: ./fototeca --page 42")

if __name__ == '__main__':
  PAGE_STEP_MAX = find_max_page_number()

  try:
    opts, args = getopt.getopt(sys.argv[1:], "h:s:p:",["help=","step=","page="])
  except getopt.GetoptError:
    print_help()
    sys.exit(2)
  
  if opts == []:
    print("Downloading..........................")
    download_data()
  else:
    for opt, arg in opts:
      if opt in ("-h", "--help"):
        print_help()
        sys.exit()
      elif opt in ("-s", "--step"):
        arg_page_step = int(arg)
        if (arg_page_step > PAGE_STEP_MAX):
          print("You exceed the number of maximum pages (" + str(PAGE_STEP_MAX) + ")")
          sys.exit()
        else:
          PAGE_STEP_MAX = arg_page_step
          print("Downloading..........................")
          download_data()
      elif opt in ("-p", "--page"):
        arg_page = int(arg)
        if (arg_page > PAGE_STEP_MAX):
          print("You exceed the number of maximum pages (" + str(PAGE_STEP_MAX) + ")")
          sys.exit()
        else:
          print("Downloading..........................")
          download_data_from_page(arg_page)

  print("You can find the data sorted in the 'output' folder")
  print()
  print("Undownloaded articles: " + str(len(UNDOWNLOADED_ARTICLES)))
  for title, url in UNDOWNLOADED_ARTICLES:
    print("   Title: " + title)
    print("   URL: " + url)
    print()
