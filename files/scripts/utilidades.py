from time import sleep

import random
import os


class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @classmethod
    def green(cls, text):
        return cls.OKGREEN + text + cls.ENDC

    @classmethod
    def red(cls, text):
        return cls.FAIL + text + cls.ENDC


def test1():
    # test of DNS exercise
    import socket
    sleep(1)
    try:
        socket.gethostbyname('www.clientedemo.com.uy')
        return True
    except socket.gaierror as error:
        return False


def test2():
    # test of router exercise
    hostname = "192.168.1.1"
    response = os.system("ping -c 1 " + hostname + ' >/dev/null 2>&1')
    if response == 0:
        sleep(1)
        return True
    else:
        return False


def test3():
    # test of docker excercise
    import requests
    url = 'http://172.31.33.32'
    sleep(1)
    try:
        result = requests.get(url)
        if result.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.ConnectionError as error:
        return False


def print_results():
    texto = ''
    texto += 'Tarea 1 resuelta: '
    texto += Bcolors.green('OK') if test1() else Bcolors.red('NO')
    texto += '\n'
    texto += 'Tarea 2 resuelta: '
    texto += Bcolors.green('OK') if test2() else Bcolors.red('NO')
    texto += '\n'
    texto += 'Tarea 3 resuelta: '
    texto += Bcolors.green('OK') if test3() else Bcolors.red('NO')
    texto += '\n'
    os.system('clear')
    print(texto)
