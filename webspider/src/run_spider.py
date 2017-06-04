from webspider.src.spider import wsdomestic
from webspider.src.spider import skyscanner
from webspider.src.logger import log
from webspider.src.spider.skyscanner_hk import return_flight
from webspider.src.spider.skyscanner_hk import reqParam

# params will be set in here

url = "https://www.tianxun.com/oneway-ccan-csha.html?depdate=2017-05-27&cabin=Economy"

def main():
    # wsdomestic.check_web(url)
    log.v("program is starting and waiting for web respond")
    # skyscanner.check_web("", "")
    return_flight.setUrl("")
    data = reqParam
    return_flight.setParamData(data)
    return_flight.runTask()

main()

