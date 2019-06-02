from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
browser=webdriver.Chrome()
browser.get('https://web.whatsapp.com/')
wait = WebDriverWait(browser, 600)
name='"To whoom you want to send message"'
path= '//span[contains(@title,' + name + ')]'
a = wait.until(EC.presence_of_element_located((By.XPATH, path)))
a.click()
for i in range(1):
	b=browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
	b.send_keys('Your Message')
	c=browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
	c.click()
