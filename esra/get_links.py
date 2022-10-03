#import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#import requests
#from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.implicitly_wait(10)

url = 'https://www.immoweb.be/en/'  #Use this link
driver.get(url)
#time.sleep(3) #its better in a loop
#Pass the cookkie banner
cookie_button = driver.find_element(By.XPATH,'//*[@id="uc-btn-accept-banner"]').click()


def get_estate_links(x):
    #driver = webdriver.Chrome()
    #driver.get(url)
    href_links = []
    #info = driver.find_elements(By.XPATH, value='//a[@href]')
    info = driver.find_elements(By.XPATH, '//a[contains(@href, "https://www.immoweb.be/en/search/house-and-apartment/for-sale/")]')

    for element in info:
        links = element.get_attribute("href")
        if links not in href_links:
            href_links.append(links)


        # city = []
        # for element_city in href_links:
        #     links_cities = element.get_attribute("href")
        #     if links_cities not in city:
        #         city.append(links_cities)
        # print("\n".join(city))
        # print(len(city))
    print("\n".join(href_links))
    print(len(href_links))
    
# info = driver.find_element(By.CLASS_NAME,'classified')  #Gets all info in the page
# area = info.find_element(By.CLASS_NAME,'classified__information--property')  #Gets specific info in the page
# print('\n--------------\ninfo',info.text)
# print('\n--------------\narea',area.text)
    

        #print(href_links)
    
    # link = info.get_attribute("href")
    # estate_url = driver.find_element(By.XPATH, '//a[contains(@href, ""
    # for x in estate_url
    # other_links = driver.find_element(By.XPATH, '//a[contains(@href, "x")]')
get_estate_links(url)
driver.close()
    
    
    
    
    #all_estate_links = []
    #for estates in all_estate_links:
        #all_estate_links.append(other_links.text)
        #print(all_estate_links) 
    
    
    
    #for elem in info:
        #print(elem.get("href"))
 
  




     





