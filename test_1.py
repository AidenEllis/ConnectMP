from connectmp.mp import Process
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
    p1 = Process(target=do_something, connection=True)
    p2 = Process(target=track_i, args=(p1.connection,))

    p1.start()
    p2.start()
