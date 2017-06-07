from webspider.src.spider.wsdomestic import check_web
from webspider.src.spider import skyscanner
from webspider.src.logger import log

from webspider.src import run_spider

# this is the main entrance of the program

# check_web("")


log.w("test Warning")
log.e("test Error")
log.v("test Verbose")
log.i("test Info", "info")

# skyscanner.check_web("", "")

run_spider.runSkyScannerHK()
