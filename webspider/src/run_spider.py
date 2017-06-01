from webspider.src.spider import wsdomestic
from webspider.src.spider import skyscanner
from webspider.src.logger import log

url = "https://www.tianxun.com/oneway-ccan-csha.html?depdate=2017-05-27&cabin=Economy"

def main():
    # wsdomestic.check_web(url)
    log.v("program is starting and waiting for web respond")
    skyscanner.check_web("", "")

main()

