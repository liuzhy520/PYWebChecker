from webspider.src.logger import log
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

url = "https://www.skyscanner.com.hk/transport/flights/can/tyoa/170601/170630/airfares-from-guangzhou-to-tokyo-in-june-2017.html?adults=1&children=0&adultsv2=1&childrenv2=&infants=0&cabinclass=economy&rtn=1&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false&ref=home#results"
def check_web(departure, arrival):
    driver = webdriver.Chrome()
    driver.get(url)

    log.v("start running")
    try:
        element = WebDriverWait(driver, 90).until(
            EC.presence_of_element_located((By.CLASS_NAME, "big-airline"))
        )
        log.v("end driver waiting")
        time.sleep(10)

        log.v("end waiting")

        getInfo(driver)
    # except Exception as e:
    #     print(e)
    #     driver.quit()
    finally:
        time.sleep(5)
        driver.quit()

        log.v("end")

def getInfo(driver):
    articles = driver.find_elements_by_css_selector("article")
    log.v("start")
    for article in articles:
        log.v("get articles")
        # try:
        time.sleep(5)

        article.click()
        log.v("click open")
        time.sleep(5)

        popup_panel = driver.find_element_by_id("details-mobile-panel")
        log.v("found details-mobile-panel")
        # flight_content = popup_session.find_elements_by_class_name("fss-bp-itinerary")
        # print(">>>found fss-bp-itinerary")
        # count = 0
        # real_content = webdriver
        # for popup_session in popup_sessions:
        #     print(">>>found details-mobile-panel count")
        #     try:
        #         count += 1
        #         popup_session.find_element_by_class_name("fss-panel-content")
        #         real_content = popup_session
        #         break
        #     except:
        #         print(count)

        legs = popup_panel.find_elements_by_class_name("itinerary-leg")
        for leg in legs:
            time.sleep(5)
            leg.click()
            log.v("click leg")
            airlines = leg.find_elements_by_class_name("operated-by")
            for airline in airlines:
                log.i("airline", airline.text)

        prices = popup_panel.find_elements_by_class_name("price")
        for price in prices:
            log.i("price" , price.text)
        # a = popup_session.find_element_by_class_name("fss-panel-content")


            log.v("click departure")

        time.sleep(5)

        driver.find_element_by_id("fss-overlay").click()
        log.v("click close")
            # driver.find_element_by_css_selector("button").find_element_by_class_name("").click()
        # except:
        #     print(">>>exception!")
        #     time.sleep(0)


        # price = article.find_element_by_class_name("mainquote-group-price").text
        #
        # logReturn("","","","","","","", "", "", "", price)

    # print(">>>next page")
    # driver.find_elements_by_id("next").click()
    # getInfo(driver)
