import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


PATH = r"C:\Users\C24Charles.Calapini\chromedriver.exe"
options = webdriver.ChromeOptions()
#options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=options, executable_path=PATH)

product_id = "W6999600"
product_link = "https:/footlocker.com/product/~/" + product_id + ".html"

#Opens the Product Link
driver.get(product_link)
time.sleep(5)



#Try block to exit news letters
newsletter_xpath = r"/html/body/div[34]/div[1]/div[2]"
policy_xpath = r"/html/body/div[1]/div[1]/div[4]/button"
try:
    time.sleep(3)
    driver.find_element_by_xpath(newsletter_xpath)\
        .click()
    time.sleep(5)
    driver.find_element_by_xpath(policy_xpath)\
        .click()
except:
    print("No News letter")



#Clicks on selected size
#Sizing on Foot locker
# Size xpath Notice the Patterns
# - size 8 /html/body/div[1]/div[1]/main/div/div[2]/div/div/form/div[4]/fieldset/div/div[2]/label
# /html/body/div[1]/div[1]/main/div/div[2]/div/div/form/div[4]/fieldset/div/div[3]/label
#  Every increment last div increase. 
#

size = 8
#note to develop xpath adjusting feature depending on users input size.
size_xpath = r"/html/body/div[1]/div[1]/main/div/div[2]/div/div/form/div[4]/fieldset/div/div[2]/label"

#Clicks on size
time.sleep(4)
driver.find_element_by_xpath(size_xpath)\
    .click()


#ADD TO CART

addToCart_xpath = r"/html/body/div[1]/div[1]/main/div/div[2]/div/div/form/ul/li[2]/button"
addToCart_class = "Button ProductDetails-form__action"

time.sleep(4)
driver.find_element_by_xpath(addToCart_xpath)\
    .click()

time.sleep(3600)
driver.quit()

