
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
