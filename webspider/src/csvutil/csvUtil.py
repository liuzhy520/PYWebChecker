from webspider.src.spider.entity import return_entity
import csv

returnEntity = return_entity

returnFieldnames = ['departairline', 'departflightno', 'departtime', 'departairport', 'arrivetime'
    , 'arriveairport', 'returnairline', 'returndepartflightno', 'returndeparttime'
    , 'returndepartairport', 'returnarrivetime', 'returnarriveairport', 'cheapestprice1', 'cheapestprice2']



# fieldnames = ['aaa', 'bbb']

filename = ""
def createReturnFile(f):
    filename = f
    with open(''+filename+'.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=returnFieldnames)
        writer.writeheader()

    return ""

def writeReturnEntity(returnEntity):
    with open(''+filename+'.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([returnEntity.departairline
                            , returnEntity.departflightno
                            , returnEntity.departtime
                            , returnEntity.departairport
                            , returnEntity.arrivetime
                            , returnEntity.arriveairport
                            , returnEntity.returnairline
                            , returnEntity.returndepartflightno
                            , returnEntity.returndeparttime
                            , returnEntity.returndepartairport
                            , returnEntity.returnarrivetime
                            , returnEntity.returnarriveairport
                            , returnEntity.cheapestprice1
                            , returnEntity.cheapestprice2
                            ])

    return returnEntity