from connectmp.mp import Process
from connectmp.connection import Connection
import time


def do_something(connection):
    for i in range(50):
        print(f"Doing something {i}")
        connection.data = i
        time.sleep(1)


def track_i(connection):
    for i in range(50):
        print(f"Track i: {connection.data}")
        time.sleep(0.5)


if __name__ == '__main__':
    c = Connection()
    p1 = Process(target=do_something, args=(c,))
    p2 = Process(target=track_i, args=(c,))

    p1.start()
    p2.start()
