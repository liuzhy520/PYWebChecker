import datetime

def logSep():
    print("=======================================================")

def i(key, value):
    print('\033[0m' + datetime.datetime.now().ctime() + ">>> " + key + " : " + value)

def e(msg):
    print('\033[31m' + datetime.datetime.now().ctime() +">>> e:" + msg)

def w(msg):
    print('\033[33m' + datetime.datetime.now().ctime() +">>> w:" + msg)

def v(msg):
    print('\033[90m' + datetime.datetime.now().ctime() +">>> v:" + msg)

