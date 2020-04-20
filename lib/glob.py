#!/bin/python3

"""Configuration module

This module contains functions for loading parameters from config files

"""

from datetime import datetime
import logging
import traceback
import configparser
import json
from pathlib import Path


def init():
    global script_home
    # global checklist

    # Path definitions
    script_home = Path(__file__).resolve().parent.parent
    # checklist = dict()
    read_config()
    setup_logging()
    logging.info('Init')

def read_config():
    global config
    _CONFIG_FILE = 'config.ini'
    _DEFAULT_CONFIG = """[common]
            project = not specified
            environment = not specified
        [checklists]
            localhost = checks.json
        [http_server]
            enable = false
            address = localhost
            port = 4444
            template = template.html
        [logging]
            level = INFO
            log_dir = logs"""

    # Reads default configuration
    config = configparser.ConfigParser()
    config.read_string(_DEFAULT_CONFIG)
    # Reads config
    config_file = script_home / _CONFIG_FILE
    try:
        with open(config_file) as f:
            config.read_file(f)
    except Exception as e:
        print('Can\'t open config file. {}'.format(e))
        raise SystemExit

def setup_logging():
   # Logging setup
    log_dir = Path(config['logging']['log_dir'])
    if not log_dir.is_absolute():
        log_dir = script_home / log_dir
    log_file = log_dir.joinpath(
                    datetime.now().isoformat(timespec='seconds') + '.log')

    # Create log file
    log_dir.mkdir(exist_ok=True)
    log_file.touch(exist_ok=True)
    logging.basicConfig(filename=log_file.as_posix(),
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S %z',
                        level=getattr(logging, config['logging']['level']))
    logging.info("The script has started.")


def read_checklist(file_name):
    try:
        with open(file_name) as f:
            chk_lst = json.load(f)
    except Exception as e:
        print("Checklist file: {} \n{}".format(file_name, e))
        raise SystemExit
    else:
        return chk_lst

def _list_config():
    lst = ''
    for section in config.sections():
        lst += f'[{section}]\n'
        for param in config.items(section):
            lst += ' = '.join(param)
            lst += '\n'
        lst += '\n'
    return lst

def _print_checklist(chk_list):
    lst = json.dumps(chk_list, sort_keys=False, indent=4)
    return lst

if __name__ == '__main__' :
    init()
    print(_list_config())

