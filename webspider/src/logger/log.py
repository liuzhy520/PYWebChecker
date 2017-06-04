import datetime

flight = ""
code = ""
departureT = ""
arrivalT = ""
dAirport = ""
aAirport = ""
tax = ""
price = ""


def log(flight, code, departureT, dAirport, arrivalT, aAirport, tax, price):
    print("=======================================================")
    print("airline:" + flight)
    print("code:" + code)
    print("departureT:" + departureT)
    print("dAirport:" + dAirport)
    print("arrivalT:" + arrivalT)
    print("aAirport:" + aAirport)
    print("tax:" + tax)
    print("price:" + price)
    print("=======================================================")

def logReturn(departF, departureT, dAirport, arrivalT, aAirport,
              returnF, rDT, RDAirport, RRT, RRAirport, price):
    print("=======================================================")
    print("Departure airline:" + departF)
    print("departureT:" + departureT)
    print("dAirport:" + dAirport)
    print("arrivalT:" + arrivalT)
    print("aAirport:" + aAirport)
    print("--- return ---")
    print("Return airline:" + returnF)
    print("Return departureT:" + departureT)
    print("Return dAirport:" + dAirport)
    print("Return arrivalT:" + arrivalT)
    print("Return aAirport:" + aAirport)
    print("--- price ---")
    print("price:" + price)
    print("=======================================================")

def printLine():
    print('\033[0m' +  "=======================================================")

def i(key, value):
    print('\033[0m' + datetime.datetime.now().ctime() + ">>> " + key + " : " + value)

def e(msg):
    print('\033[31m' + datetime.datetime.now().ctime() +">>> e:" + msg)

def w(msg):
    print('\033[33m' + datetime.datetime.now().ctime() +">>> w:" + msg)

def v(msg):
    print('\033[90m' + datetime.datetime.now().ctime() +">>> v:" + msg)

