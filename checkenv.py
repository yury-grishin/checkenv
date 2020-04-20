#!/bin/python3


"""

"""

import logging
from lib import var as g

if __name__ == '__main__' :
    g.init()
    print(g._list_config())
    print(g.config['logging']['level'])
    logging.info('main')
