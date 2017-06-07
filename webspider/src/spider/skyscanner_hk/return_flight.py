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


    # PROXY = "127.0.0.1:1080"
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--proxy-server={0}'.format(PROXY))
    #
    # driver = webdriver.Chrome(chrome_options=chrome_options)

    # driver = webdriver.Chrome()


        # driver.delete_all_cookies()
    profile = webdriver.FirefoxProfile()
    profile.native_events_enabled = True
    driver = webdriver.Firefox(profile)

    driver.get(param.createReturnUrl())

        # element = WebDriverWait(driver, 90).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, "article")))
    time.sleep(30)
        # driver.implicitly_wait(30)

    log.v("end driver wait")

    getInfo(driver)

    time.sleep(200)

    # entity.print()

def getInfo(driver):
    articles = driver.find_elements_by_css_selector("article")
    log.v("found articles")

    time.sleep(5)
    log.v("end wait")
    # articles = driver.find_elements_by_class_name("day-list-item")
    log.v("start")
    log.v("get articles")
    for article in articles:
        entity = return_entity

        log.v("article start")
        time.sleep(5)
        sections = article.find_elements_by_css_selector("section")
        log.v("found sections")

        count = 0
        for section in sections:
            time.sleep(3)

            try:
                bigairline = section.find_element_by_class_name("big-airline")
                log.v("found big-airline")
            except:
                continue

            time.sleep(2)

            try:
                airline = bigairline.find_element_by_class_name("text-sm")
                log.v(airline.text)
                if count == 0:
                    entity.departairline = airline.text
                else:
                    entity.returnairline = airline.text
                log.v("found text-sm")
            except:
                try:
                    airline = bigairline.find_element_by_class_name("big")
                    log.v(airline.get_attribute("alt"))
                    if count == 0:
                        entity.departairline = airline.get_attribute("alt")
                    else:
                        entity.returnairline = airline.get_attribute("alt")
                    log.v("found img")
                except:
                    continue
            finally:
                log.v("count:" + str(count))
                count = count + 1



        entity.print()
        log.v("article end")


