from webspider.src.spider import wsdomestic
from webspider.src.spider import skyscanner

url = "https://www.tianxun.com/oneway-ccan-csha.html?depdate=2017-05-27&cabin=Economy"

def main():
    # wsdomestic.check_web(url)
    skyscanner.check_web("", "")

main()

