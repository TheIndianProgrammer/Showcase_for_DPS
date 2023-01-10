from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "G:\Programming\Chrome\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://google.com")

search = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input') 
search.send_keys("Virat Kholi")
time.sleep(2)
search.send_keys(Keys.RETURN)

time.sleep(3)
s1 = driver.find_element_by_xpath('//*[@id="wp-tabs-container"]/div[2]/div/div/div/div[2]')
search = driver.find_element_by_xpath('/html/body/div[7]/div/div[9]/div[2]/div/div/div[2]/div[5]/div/div/div/div[1]/div/div/div/div/div[1]/div/div/div/span[1]')

print(s1.text)
print(search.text)
