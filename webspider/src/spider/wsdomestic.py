from webspider.src.logger.logger import log
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# check domestic flights

isDone = 0
def check_web(url):
    driver = webdriver.Chrome()
    driver.get(url)
    delay = 100  # seconds

    time.sleep(5)
    # driver.find_element_by_class_name("title".index(0)

    try:
        if(driver.find_elements_by_class_name("title").__getitem__(0).text == "访问异常"):
            print(driver.find_elements_by_class_name("title").__getitem__(0).text)
            time.sleep(10)
        else:
            time.sleep(3)
    except:
        time.sleep(3)


    goflights = driver.find_element_by_id("go-flights")

    listcon = goflights.find_elements_by_class_name("list_con")

    for con in listcon:
        try:
            price = con.find_element_by_class_name("pricefield").text

            name = con.find_element_by_class_name("airline").text

            dt = con.find_element_by_class_name("box2").find_element_by_class_name("fs14").text

            da = con.find_element_by_class_name("box2").find_element_by_css_selector("span").text

            at = con.find_element_by_class_name("box4").find_element_by_class_name("fs14").text

            aa = con.find_element_by_class_name("box4").find_element_by_css_selector("span").text

            tax = con.find_element_by_class_name("tax").text

            code = con.find_element_by_class_name("aircraft").text
        except:
            price = ""
            name = ""
            dt = ""
            da = ""
            at = ""
            aa = ""
            tax = ""
            code = ""
        log(name, code, dt, da, at, aa, tax, price)

    # for i in price:
    #     print(i.text)

    time.sleep(200)
    # try:
    #     WebDriverWait(driver, delay)
    #     # price = driver.find_element_by_class_name("pricefield")
    #     # print(price)
    #
    # except TimeoutException:
    #     print("Loading took too much time!")

    # price = driver.find_element_by_class_name("pricefield")
    #
    # print(price)