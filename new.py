from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep

def scroll_page():
    for i in range(7):
        webdriver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(3)

def click_button():
    more_imgs_button_xpath = '/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div[1]/div[2]/div[2]/input'
    driver.find_element_by_xpath(more_imgs_button_xpath).click()   

