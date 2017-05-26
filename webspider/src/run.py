from webspider.src.spider import wsdomestic

url = "https://www.tianxun.com/oneway-ccan-chgh.html?depdate=2017-05-26&cabin=Economy"

def main():
    wsdomestic.check_web(url)


main()