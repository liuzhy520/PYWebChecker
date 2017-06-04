from selenium import webdriver

PROXY = "123.56.92.104:8118"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server={0}'.format(PROXY))
chrome = webdriver.Chrome(chrome_options=chrome_options)
chrome.get('http://1212.ip138.com/ic.asp')
print('2: ', chrome.page_source)
# chrome.quit()