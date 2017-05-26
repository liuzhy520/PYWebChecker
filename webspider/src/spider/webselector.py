from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

isDone = 0

def check_web(url):
    driver = webdriver.Chrome()
    driver.get(url)
    delay = 100  # seconds

    time.sleep(5)
    # driver.find_element_by_class_name("title".index(0)

    print(driver.find_elements_by_class_name("title").__getitem__(0).text)
    if(driver.find_elements_by_class_name("title").__getitem__(0).text == "访问异常"):
        time.sleep(10)

    goflights = driver.find_element_by_id("go-flights")

    listcon = goflights.find_elements_by_class_name("list_con")

    for con in listcon:
        price = con.find_element_by_class_name("pricefield")
        name = con.find_element_by_class_name("airline")
        code = con.find_element_by_class_name("aircraft")
        print("flight:" + name.text + " | code:" + code.text + " | price:￥" + price.text)

    # for i in price:
    #     print(i.text)

    time.sleep(200)
    try:
        WebDriverWait(driver, delay)
        # price = driver.find_element_by_class_name("pricefield")
        # print(price)

    except TimeoutException:
        print("Loading took too much time!")

    # price = driver.find_element_by_class_name("pricefield")
    #
    # print(price)