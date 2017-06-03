from webspider.src.logger import log

# departairline
# departflightno
# departtime
# departairport
# arrivetime
# arriveairport
# return departtime
# return departairport
# return arrivetime
# return arriveairport
# cheapestprice1
# cheapestprice2

departairline = ""
departflightno = ""
departtime = ""
departairport = ""
arrivetime = ""
arriveairport = ""
returndepartairline = ""
returndepartflightno = ""
returndeparttime = ""
returndepartairport = ""
returnarrivetime = ""
returnarriveairport = ""
cheapestprice1 = ""
cheapestprice2 = ""


def __init__(self):
    return self

def print():
    log.printLine()
    log.i("depart airline", departairline)
    log.i("depart flight no", departflightno)
    log.i("depart time", departtime)
    log.i("depart airport", departairport)
    log.i("arrive airport", arriveairport)
    log.i("arrive time", arrivetime)

    log.i("return depart airline", returndepartairline)
    log.i("return depart flight no", returndepartflightno)

    log.i("return depart time", returndeparttime)
    log.i("return depart airport", returndepartairport)
    log.i("return arrive airport", returnarriveairport)
    log.i("return arrive time", returnarrivetime)
    log.i("cheap price 1", cheapestprice1)
    log.i("cheap price 2", cheapestprice2)
    log.printLine()





