#!/bin/python3

"""Main module

Environment checklist

"""

import logging
from lib import glob as g

if __name__ == '__main__':
    g.init()
    print(g._list_config())
    # print(g.config['logging']['level'])
    # logging.info('main')
