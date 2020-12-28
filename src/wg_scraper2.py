from selenium import webdriver
import time
from bs4 import BeautifulSoup
import csv

profile = webdriver.FirefoxProfile()
driver = webdriver.Firefox(firefox_profile=profile)
profile.set_preference("permissions.default.image", 2)
soup = BeautifulSoup('html.parser')
counter = 0
ad_set = []

page_no = 0


def scraper():
  for ad in range(3):
    #go to page
    global page_no
    url = 'https://www.wg-gesucht.de/wg-zimmer-in-Munster.91.0.1.' + str(page_no) + '.html'
    driver.get(url)
    page_no += 1

    #click accept all
    try:
      driver.find_element_by_xpath('//*[@id="cmpbntyestxt"]').click()
    except:
      pass

    eList = driver.find_element_by_xpath('//*[@id="main_column"]')

    print(str(eList))
    hrefList = []
    for e in eList:
        hrefList.append(e.get_attribute('href'))

    for href in hrefList:
      print(str(href))




scraper()