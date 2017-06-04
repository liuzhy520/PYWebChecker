from selenium import webdriver
from webspider.src.proxy.ip_list import ips

PROXY = ips[1]
print(PROXY)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server={0}'.format(PROXY))
chrome = webdriver.Chrome(chrome_options=chrome_options)

# chrome = webdriver.Chrome()

chrome.get('http://www.ip138.com/')
print('2: ', chrome.page_source)
# chrome.quit()