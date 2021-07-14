from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import requests
import os 

def scroll_page():
    for i in range(7):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(3)

def click_button():
    more_imgs_button_xpath = '/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div[1]/div[2]/div[2]/input'
    driver.find_element_by_xpath(more_imgs_button_xpath).click()   

def find_images():  
    html_source = driver.page_source
    soup = BeautifulSoup(html_source, 'html.parser')

    imgs_urls = []
    for img in soup.find_all('img'):
        try:
            if img['src'].startswith('http'):
                imgs_urls.append(img['src'])
        except:
            pass 

    return imgs_urls

#create webdriver
driver = webdriver.Chrome(executable_path="./driver/chromedriver")

#define url 
url = "https://www.google.com/search?q={}&site=webhp&tbm=isch".format("computer")

#get url 
driver.get(url)

#keo den khi nao nhan vao nut them anh 
scroll_page()
click_button()
#tim anh 
img_urls = find_images()

#dong driver
driver.close()

# print(img_urls)

#download
def download(folder):
    os.mkdir(folder)
    for i in range(len(img_urls)):
        response = requests.get(img_urls[i])
        name = "image{}".format(i)
        file = open("./image/"+name+".png", "wb")
        file.write(response.content)
        file.close()

download("image")

