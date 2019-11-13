import sys
import os
import argparse
from logging_config import Config
import logging
import logging.config

def main(sys_argv):
    parser = argparse.ArgumentParser(description="This application does nothing.")
    parser.add_argument("-n", "--nothing", type=int, default=0, help="This is Nothing")
    parser.add_argument("-z", "--zenzen", action="store_true", help="Zenzen desu yo")
    parser.add_argument("--nada", type=str, nargs= 2, dest="nada", help="Esto no es nada")
    args = parser.parse_args()

    # To retrieve args:
    args.nothing
    args.zenzen
    args.nada

    # Logging Setup
    config = Config()
    logging.config.dictConfig(config.config)

if __name__ == '__main__':
    main(sys.argv[1:])