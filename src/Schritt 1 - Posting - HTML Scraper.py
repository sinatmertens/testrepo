"""HTML Scraper written by Sina Mertens on October 22th 2020"""
# This scraper scrapes the HTMl of all postings of a given Instagram Hashtag

import argparse
from datetime import datetime
import time
import os
import csv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
from lxml import html
import requests

# Variables:
hashtag = 'schwerte'
# General settings
#firefox_options = webdriver.FirefoxOptions()

# Disabling Images in Firefox
profile.set_preference("permissions.default.image", 2)
driver.implicitly_wait(8)
soup = BeautifulSoup('html.parser')
counter = 0
get_hashtag_user_set = []

def setUp():
  # Starting the webdriver
  profile = webdriver.FirefoxProfile()
  driver = webdriver.Firefox(firefox_profile=profile)
  driver.implicitly_wait(10)

def tear_down():
  # Stop webdriver
  driver.quit()

def go_to_page(url):
    # Open URL
    try:
        driver.get(url)
    except NoSuchElementException as ex:
        fail(ex.msg)

def login(username, password):
  # Login to Instagram
  print('Loggin in')
  driver.find_element_by_xpath(
    "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input").send_keys(username)
  driver.find_element_by_xpath(
    "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input").send_keys(password)
  time.sleep(2)
  driver.find_element_by_xpath("//button[contains(.,'Accept')]").click()
  time.sleep(2)
  driver.find_element_by_xpath("//button[contains(.,'Log In')]").click()
  time.sleep(2)
  driver.find_element_by_xpath("//button[contains(.,'Not Now')]").click()

def open_hashtag_url():
    # Opens up the small hashtag Window
    go_to_page("https://www.instagram.com/explore/tags/" + hashtag + "/")
    time.sleep(1)

    #open the small window
    get_posting_html = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]")
    get_posting_html.click()
    time.sleep(1)

    print('Start of Scraping:' + str(datetime.now()))

def start_scraping(config):
  global get_posting_html
  global hashtag
  username = ('planertum')
  password = ('Herbstwetter92')

  go_to_page("https://www.instagram.com/")
  login(username, password)

  open_hashtag_url()
  get_posting_html = get_posting_html()
  output_csv()

def get_posting_html():
  for user in range(10):

    table = {}

    el = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div')
    time.sleep(1)
    table['html'] = el.get_attribute('innerHTML')

    # Counter telling me, which Account Nr. got scraped so far.
    global counter
    counter = counter + 1
    print('Account Nr. ' + str(counter) + ' saved.')

    try:
      # Hit the next button or stop the loop, if there is none.
      next_button = driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a[2]')
      next_button.click()
      time.sleep(3)
      get_hashtag_user_set.append(table)
    except:
      print('No next button!')
      break



def output_csv():
  with open("2020-10-30-_postings_" + hashtag + '.csv', "w+", newline='') as f:
    # Saving the data inside the csv file
    w = csv.DictWriter(f, ['html'])
    w.writeheader()
    for table in get_hashtag_user_set:
      w.writerow(table)

if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    config = parser.parse_args()

    start_scraping(config)

    os.system('say "your program has finished"')