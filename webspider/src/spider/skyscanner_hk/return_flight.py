from webspider.src.logger import log
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webspider.src.spider.entity import return_entity
from webspider.src.spider.skyscanner_hk import reqParam
import time

# returning flight

mUrl = ""
param = reqParam
entity = return_entity


def setParamData(data):
    param = data
    mUrl = data.createReturnUrl()
    log.v(param.createReturnUrl())



def runTask():

    # try:
    #
    #     PROXY = "127.0.0.1:1080"
    #     chrome_options = webdriver.ChromeOptions()
    #     chrome_options.add_argument('--proxy-server={0}'.format(PROXY))
    #     driver = webdriver.Chrome(chrome_options=chrome_options)
    #
    #     # driver = webdriver.Chrome()
    #
    #     driver.get(param.createReturnUrl())
    #
    #     # element = WebDriverWait(driver, 90).until(
    #     #     EC.presence_of_element_located((By.CSS_SELECTOR, "article")))
    #     time.sleep(20)
    #     # driver.implicitly_wait(30)
    #     articles = driver.find_elements_by_css_selector("article")
    #     log.v("found articles")
    #     log.v("end driver wait")
    #     time.sleep(5)
    #     log.v("end wait")
    #
    #     getInfo(articles)
    # finally:
    #     time.sleep(10)
    #     driver.quit()
    # #


    PROXY = "127.0.0.1:1080"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server={0}'.format(PROXY))

    driver = webdriver.Chrome(chrome_options=chrome_options)

    # driver = webdriver.Chrome()


        # driver.delete_all_cookies()

    driver.get(param.createReturnUrl())

        # element = WebDriverWait(driver, 90).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, "article")))
    time.sleep(20)
        # driver.implicitly_wait(30)


    getInfo(driver)

    time.sleep(200)

    # entity.print()

def getInfo(driver):
    articles = driver.find_elements_by_css_selector("article")
    log.v("found articles")
    log.v("end driver wait")
    time.sleep(5)
    log.v("end wait")
    # articles = driver.find_elements_by_class_name("day-list-item")
    log.v("start")
    for article in articles:
        log.v("get articles")
        time.sleep(3)
        sections = article.find_elements_by_css_selector("section")
        log.v("found sections")

        for section in sections:
            time.sleep(3)

            bigairline = section.find_element_by_class_name("big-airline")
            log.v("found big-airline")
            try:
                airline = bigairline.find_element_by_class_name("text-sm")
                log.v(airline.text)
                log.v("found text-sm")
            except:
                airline = bigairline.find_elements_by_css_selector("img")
                log.v(airline.text)
                log.v("found img")






