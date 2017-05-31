from webspider.src.logger.logger import log, logReturn
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

url = "https://www.skyscanner.com.hk/transport/flights/can/tyoa/170528/170529/airfares-from-guangzhou-to-tokyo-in-may-2017.html?adults=1&children=0&adultsv2=1&childrenv2=&infants=0&cabinclass=economy&rtn=1&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false&ref=home#results"

def check_web(departure, arrival):
    driver = webdriver.Chrome()
    driver.get(url)

    time.sleep(20)

    try:
        getInfo(driver)
    except:
        print(">>>exception! retry!")
        time.sleep(3)
        getInfo(driver)

    time.sleep(200)

    print("emd")

def getInfo(driver):
    articles = driver.find_elements_by_css_selector("article")
    print(">>>start")
    for article in articles:

        try:
            time.sleep(3)

            article.click()
            print(">>>click open")
            time.sleep(5)

            popup_session = driver.find_element_by_class_name("fss-popup")
            print(">>>found fss-popup")
            flight_content = popup_session.find_element_by_class_name("fss-bp-itinerary")
            print(">>>found fss-bp-itinerary")
            a = popup_session.find_element_by_class_name("operated-by")
            print(">>>found operated-by")
            print(">>>click departure")

            time.sleep(5)

            driver.find_element_by_id("fss-overlay").click()
            print(">>>click close")
            # driver.find_element_by_css_selector("button").find_element_by_class_name("").click()
        except:
            print(">>>exception!")
            time.sleep(0)


        # price = article.find_element_by_class_name("mainquote-group-price").text
        #
        # logReturn("","","","","","","", "", "", "", price)
