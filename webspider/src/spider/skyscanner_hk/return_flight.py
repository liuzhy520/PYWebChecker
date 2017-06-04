from webspider.src.logger import log
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webspider.src.spider.entity import return_entity
from webspider.src.spider.skyscanner_hk import reqParam

# returning flight

mUrl = ""
param = reqParam
entity = return_entity

def setUrl(url):
    mUrl = url

    entity.departairline = "diunee"

def setParamData(data):
    param = data
    log.e(param.createReturnUrl())



def runTask():


    entity.print()
    log.v("diunee")