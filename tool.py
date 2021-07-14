from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep


def scrape_all_imgs_google(searchTerm):
    def scroll_page():
        for i in range(7):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(3)

    def click_button():
        more_imgs_button_xpath = '/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div[1]/div[2]/div[2]/input'
        driver.find_element_by_xpath(more_imgs_button_xpath).click()   

    # def create_soup():
       
    def find_imgs():
        html_source = driver.page_source
        soup = BeautifulSoup(html_source, 'html.parser')

        imgs_urls = []
        for img in soup.find_all('img'):
            try:
                if img['src'].startswith('http'):
                    imgs_urls.append(img['src'])
            except:
                pass

    #create webdriver
    driver = webdriver.Chrome(executable_path="./driver/chromedriver")

    #define url using search term
    searchUrl = "https://www.google.com/search?q={}&site=webhp&tbm=isch".format(searchTerm)

    #get url
    driver.get(searchUrl)

    try:
        click_button()
        scroll_page()
    except:
        scroll_page()
        click_button()   

    # #create soup only after we loaded all imgs when we scroll'ed the page down
    # create_soup()

    #find imgs in soup
    find_imgs()

    #close driver
    driver.close()

    #return list of all img urls found in page

urls = scrape_all_imgs_google('computer')
print(len(urls))