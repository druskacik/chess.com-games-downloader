from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

base_url = 'https://www.chess.com/games/archive/funo09?show=live_blitz&gameType=live_blitz&rated=rated&page='
number_of_pages = 16

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()

for i in range(1, number_of_pages + 1):
  url = base_url + str(i)

  driver.get(url)

  checkbox = driver.find_element_by_class_name("archive-games-check-all")
  checkbox.click()

  download_button = driver.find_element_by_class_name("archive-games-download-button")
  download_button.click()

  time.sleep(2)
