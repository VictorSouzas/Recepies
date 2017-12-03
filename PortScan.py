# -*- coding: utf-8 -*-

import argparse
from socket import *

parser = argparse.ArgumentParser()
parser.add_argument("ip", help="ip portNumber")
parser.add_argument("port", type=int, help="ip portNumber")
args = parser.parse_args()


def conn_scan(host, port):
    try:
        connSocket = socket(AF_INET, SOCK_STREAM)
        connSocket.connect(host + port)
        print("%d tcp port open\n", port)
        connSocket.close()
    except:
        pass


def port_scan(host, ports):
    try:
        target_ip = gethostbyname(host)
    except:
        print("Can't resolve '%s'", host)
        return
    try:
        target_name = gethostbyaddr(target_ip)
        print("Scan results for " + target_name)
    except:
        print("Scan results for " + target_ip)
    setdefaulttimeout(1)
    for port in ports:
        conn_scan(target_ip, port)
