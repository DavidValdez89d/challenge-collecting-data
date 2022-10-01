from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('/home/piero/.local/bin/chromedriver')
driver.implicitly_wait(10)

url = 'https://www.immoweb.be/en/search'  #Use this link
driver.get(url)

#Pass the cookkie banner
cookie_button = driver.find_element(By.XPATH,'//*[@id="uc-btn-accept-banner"]').click()