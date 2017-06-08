from webspider.src.logger import log
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webspider.src.spider.entity import return_entity
from webspider.src.spider.skyscanner_hk import reqParam
import time
from webspider.src.csvutil import csvUtil
import datetime

# returning flight

mUrl = ""
param = reqParam
entity = return_entity
csvU = csvUtil

def setParamData(data):
    param = data
    mUrl = data.createReturnUrl()
    log.v(param.createReturnUrl())






def runTask():
    filename = param.departCityCode + "-" + param.arriveCityCode + "-" + param.departDate + "-" + param.returnDate + "-"
    csvUtil.filename = filename
    csvUtil.createReturnFile(filename)
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
    time.sleep(50)
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
        time.sleep(2)
        sections = article.find_elements_by_css_selector("section")
        log.v("found sections")

        count = 0
        for section in sections:
            # time.sleep(3)

            try:
                bigairline = section.find_element_by_class_name("big-airline")
                log.v("found big-airline")
            except:
                continue

            # time.sleep(1)

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

            try:
                # time.sleep(1)
                stations = section.find_elements_by_class_name("station-tooltip")
                log.v("found station-tooltip")
                for i in range(2):
                    times = stations.__getitem__(i).find_element_by_class_name("times")
                    airport = stations.__getitem__(i).find_element_by_class_name("stop-station")
                    log.v("time:" + times.text)
                    log.v("airport:" + airport.text)
                    if count == 0:
                        if i == 0 :
                            entity.departtime = times.text
                            entity.departairport = airport.text
                        else:
                            entity.arrivetime = times.text
                            entity.arriveairport = airport.text
                    else:
                        if i == 0 :
                            entity.returndeparttime = times.text
                            entity.returndepartairport = airport.text
                        else:
                            entity.returnarrivetime = times.text
                            entity.returnarriveairport = airport.text

            except:
                continue
            finally:
                count = count + 1
                log.v("section end")


        price = article.find_element_by_class_name("mainquote-price")
        log.v("price:"+price.text)

        entity.cheapestprice1 = price.text

        entity.print()
        csvUtil.writeReturnEntity(entity)
        log.v("article end")


