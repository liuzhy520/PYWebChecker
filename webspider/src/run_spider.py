from webspider.src.spider import wsdomestic
from webspider.src.spider import skyscanner
from webspider.src.logger import log
from webspider.src.spider.skyscanner_hk import return_flight
from webspider.src.spider.skyscanner_hk import reqParam

# params will be set in here

# url = "https://www.tianxun.com/oneway-ccan-csha.html?depdate=2017-05-27&cabin=Economy"
data = reqParam

# data.url = "https://www.skyscanner.com.hk/transport/flights/can/mela/170611/170708/airfares-from-guangzhou-to-melbourne-in-june-2017-and-july-2017.html?adults=1&children=0&adultsv2=1&childrenv2=&infants=0&cabinclass=economy&rtn=1&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false&ref=home#results"
def main():

    log.v("program is starting and waiting for web respond")

    return_flight.setParamData(data)
    return_flight.runTask()


def runSkyScannerHK():
    log.v("start to run")
    if data.returnDate.__eq__("") | data.departDate.__eq__("") | data.departCityCode.__eq__("") | data.arriveCityCode.__eq__(""):
        log.v("invalid param")
        return
    return_flight.setParamData(data)
    return_flight.runTask()

def setReturnParams(departure, destination, departDate, returnDate):
    data.departCityCode = departure
    data.arriveCityCode = destination
    data.departDate = departDate
    data.returnDate = returnDate