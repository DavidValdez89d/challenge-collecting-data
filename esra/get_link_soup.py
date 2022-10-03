import json
import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


url = 'https://www.immoweb.be/en/'  #Use this link

#time.sleep(3) #its better in a loop
#Pass the cookkie banner


def get_page_links(url):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(url)

    driver.find_element(By.XPATH,'//*[@id="uc-btn-accept-banner"]').click()

    
    
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    s_links = soup.select('li.search-results__item a')
        
    url_list = list()
    for element in s_links:
        link = element["href"]
        if '/agency' in link or '/en/classified/' not in link: 
            pass
    
        elif 'https://www.immoweb.be' not in link:
            link = 'https://www.immoweb.be' + link
            url_list.append(link)
        else:
            url_list.append(link)
    return url_list
    
    
    
def main():
    all_urls = list()
    property_type = ['house', 'apartment']
    for x in range(1,2):
        for type in property_type:
            urls = get_page_links(f'https://www.immoweb.be/en/search/{type}/for-sale?countries=BE&page={x}&orderBy=relevance')
        
        for url in urls:
            if url not in all_urls:
                all_urls.append(url)  

    print(len(all_urls))  
    with open('url_data_seperated.json','w') as fd:
        json.dump(all_urls, fd)
    print("JSON file saved.")    
    
        
    return all_urls

print(main())
