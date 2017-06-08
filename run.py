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

departure = "can"       # departure airport code
destination = "sha"     # destination airport code

departDate = "170613"   # depart date (format: YYMMDD)
returnDate = "170701"   # arrive date (format: YYMMDD)

run_spider.setReturnParams(departure, destination, departDate, returnDate)

run_spider.runSkyScannerHK()
