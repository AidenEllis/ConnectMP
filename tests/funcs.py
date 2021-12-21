import time
from .exceptions import DataMatchedException


def do_something(connection, data):
    time.sleep(1)
    connection.data = data


def track_i(connection, data):
    time.sleep(2)
    if connection.data == data:
        raise DataMatchedException(data)
