from webspider.src.spider import webselector

url = "https://www.tianxun.com/oneway-ccan-csha.html?depdate=2017-05-26&cabin=Economy"

def main():
    webselector.check_web(url)


main()