from selenium import webdriver
import time

driver = webdriver.Chrome()

url = 'http://c.m.163.com/news/l/107212.html?w=4'

count = 12
driver.get(url)
while count > 0:
    driver = webdriver.Chrome()
    for j in range(5):

        driver.execute_script('''window.open("%s","_blank");''' % url)
        # driver.refresh()
        print('%s %d' % ('count :', count))
        count = count - 1

    driver.close()
    time.sleep(5)
    driver.quit()

    print('close')

