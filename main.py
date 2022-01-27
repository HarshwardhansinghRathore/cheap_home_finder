import requests
import bs4
import lxml
import pdb
from selenium import webdriver
import time
headers = {
    "Accept-Language": 'en-US,en;q=0.9,hi-IN;q=0.8,hi;q=0.7',
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}
response = requests.get('https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.87415541601563%2C%22east%22%3A-121.79474867773438%2C%22south%22%3A37.49547144437709%2C%22north%22%3A38.13187358858673%7D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D', headers=headers)
beautiful_text = response.text
beautiful_html = bs4.BeautifulSoup(beautiful_text, 'lxml')

a_tags = beautiful_html.select(selector='.list-card-top a')
f_a = [a.get('href') for a in a_tags]
for item in f_a:
    if item[0:4] != 'http':
        copy = item
        item = f"https://www.zillow.com{copy}"
prices = beautiful_html.select(selector='div .list-card-price')
f_prices = [price.text for price in prices]

locations_tag = beautiful_html.select(selector=".list-card-addr")
f_addr = [addr.text for addr in locations_tag]


forms_url = 'https://docs.google.com/forms/d/e/1FAIpQLSdG20ch_nOxN_IMhJpocN2TNMsWj8woDVhfiKh7vNtW_TVhHQ/viewform?usp=sf_link'
driver = webdriver.Chrome(executable_path='C:\\Users\\hrath\\Downloads\\chromedriver_win32\\chromedriver')
driver.get(forms_url)

for n in range(1):
    time.sleep(3)
    addr_q = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    addr_q.send_keys(f_addr[n])
    price_q = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_q.send_keys(f_prices[n])
    link_q = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_q.send_keys(f_a[n])
    submit_form_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit_form_button.click()
    time.sleep(5)