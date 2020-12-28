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

def go_to_page(url, city):
  #open URL
  driver.get(url)
  #click on the city window
  driver.find_element_by_xpath('//*[@id="autocompinp"]').send_keys(city)
  try:
    driver.find_element_by_xpath('//*[@id="cmpbntyestxt"]').click()
  except:
    pass

  #click to open dropdown
  driver.find_element_by_xpath('//*[@id="categories"]/div[2]/button/div').click()
  #click to pick wg
  driver.find_element_by_xpath('//*[@id="categories"]/div[2]/div/div/ul/li[1]').click()
  driver.find_element_by_xpath('//*[@id="categories"]/div[2]/div/div/ul/li[2]').click()
  #click on finden
  driver.find_element_by_xpath('//*[@id="search_button"]').click()
  time.sleep(5)

def go_to_page_shortcut():
  driver.get('https://www.wg-gesucht.de/wg-zimmer-in-Aachen.1.0.1.0.html')
  time.sleep(3)

def get_ad():
  time.sleep(3)
  driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[6]/div[1]/div[4]/div/div[1]').click()

def scraping():
  for ad in range(3):

    table = {}

    el = driver.find_element_by_xpath('//*[@id="main_column"]')
    time.sleep(1)
    table['html'] = el.get_attribute('innerHTML')
    global counter
    counter = counter + 1
    print('Ad No. ' + str(counter) + ' saved.')

    try:
      # Hit the next button or stop the loop, if there is none.
      #next_button = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[4]/div[1]/nav[1]/div/div[3]/a/span[1]')
      #next_button.click()
      time.sleep(5)
      next_button_2 = driver.find_element_by_xpath("//span[text()='Continue']").click()
      next_button_2.click()
    except:
      print('No next button!')
      break

    ad_set.append(table)

def output_csv(city):
  with open('test' + city + '.csv', "w+", newline='') as f:
    # Saving the data inside the csv file
    w = csv.DictWriter(f, ['html'])
    w.writeheader()
    for table in ad_set:
      w.writerow(table)







go_to_page_shortcut()
get_ad()
scraping()
output_csv("Aachen")
