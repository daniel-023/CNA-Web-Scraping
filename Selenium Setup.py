from selenium import webdriver
import requests
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get('https://www.channelnewsasia.com/latest-news')
webpage = driver.page_source
soup = BeautifulSoup(webpage, 'html.parser')
print(soup.prettify())