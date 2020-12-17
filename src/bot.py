from collections import defaultdict
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import random
import time
import re
import collections
import sys


class Bot:

    #start webdriver
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--start-fullscreen')
        #chrome_options.add_argument('--no-sandbox')
        #chrome_options.add_argument('--headless')
        #chrome_options.add_argument('--disable-gpu')
        self.times_restarted = 0
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.implicitly_wait(10)

    #stop webdriver
    def tear_down(self):
        self.driver.quit()

    #Open URL
    def go_to_page(self, url):
        try:
            self.driver.get(url)
        except NoSuchElementException as ex:
            self.fail(ex.msg)

    def get_location_info(self):
        self.go_to_page("https://www.yelp.de/search?find_desc=Restaurants&find_loc=Dortmund+Marten&ns=1")
        time.sleep(3)
        get_location_info_set = set()
        time.sleep(3)
        get_location_info_set = set()
        time.sleep(2)

        #open the small window
        get_location_info = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]")
        get_location_info.click()
        time.sleep(2)
        #usernames = self.driver.find_elements_by_xpath("/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]")

        #date = self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/div[2]')
        #date = date.find_element_by_tag_name('a')
        #time.sleep(2)
        #dateis = date.get_attribute('title')
        #lastdate = '2018'
        next_button = self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]')

        for user in range(139):

            #find username
            el = self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]')
            el = el.find_element_by_tag_name('a')
            time.sleep(2)
            profile = el.get_attribute('href')

            #find datime
            el2 = self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/div[2]')
            el2 = el2.find_element_by_tag_name('time')
            time.sleep(2)
            datetime = el2.get_attribute('datetime')

            #find postinglink
            el3 = self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/div[2]')
            el3 = el3.find_element_by_tag_name('a')
            time.sleep(2)
            postinglink = el3.get_attribute('href')
            get_hashtag_user_set.add(profile + " " + datetime + " " + postinglink)

            #next_button = self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]')
            next_button.click()
            time.sleep(2)


        return list(get_location_info_set)
