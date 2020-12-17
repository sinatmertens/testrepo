from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

class Bot:

  # start webdriver
  def set_up(self):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--start-fullscreen')
    self.times_restarted = 0
    self.driver = webdriver.Chrome(chrome_options=chrome_options)
    self.driver.implicitly_wait(10)

    # stop webdriver
    def tear_down(self):
      self.driver.quit()

    # Open URL
    def go_to_page(self, url):
      try:
        self.driver.get(url)
      except NoSuchElementException as ex:
        self.fail(ex.msg)

    def pick_city(self, city):
      self.driver.find_element_by_xpath('//*[@id="autocompinp"]').send_keys(city)
      self.driver.find_element_by_xpath('//*[@id="search_button"]').click()

    def get_ad(self):
      time.sleep(3)
      # ""