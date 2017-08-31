from threading import Thread
from sys import exit
from time import sleep
from subprocess import Popen, PIPE

class Ping:
    def __iter__(self):
        for line in Popen(['ping', '-c1', 'google.com'], stdout=PIPE).stdout.readlines():
            yield line


def display_ping():
    while True:
        ping = yield 'Waiting...'
        print(ping)

def retry(func):
    def wrapper():
        while True:
            func()
        return func
    return wrapper

@retry
def run():
    display = display_ping()
    print(next(display))
    pinger = Ping()
    for line in pinger:
        display.send(line)

ping = Thread(target=run)
ping.start()

