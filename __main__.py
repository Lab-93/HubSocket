#!/bin/python3


"""
"""


from __init__ import *
from argparse import ArgumentParser


if __name__ == "__main__":
    arguments = ArgumentParser()
    arguments.add_argument( "-H", "--host", default="127.0.0.1"                    )
    arguments.add_argument( "-P", "--port", default=65535                          )
    arguments.add_argument( "-L", "--logfile", default="/server/logs/LiveData.log" )

    arguments = arguments.parse_args()

    while True:
        apiHub(arguments.host, int(arguments.port))


