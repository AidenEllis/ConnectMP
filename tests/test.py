import unittest
from connectmp import Process, Connection
from tests.funcs import do_something, track_i
from tests.exceptions import DataMatchedException


class TestConnectMP(unittest.TestCase):

    def test_process_connection(self):
        data = 26127

        p1 = Process(target=do_something, connection=True, kwargs={'data': data})
        p2 = Process(target=track_i, args=(p1.connection, data))

        p1.start()
        p2.start()

        self.assertRaises(DataMatchedException)

    def test_connection(self):
        data = "Crabby Patty's Secret Formula!"

        connection = Connection()

        p1 = Process(target=do_something, args=(connection, data))
        p2 = Process(target=track_i, args=(connection, data))

        p1.start()
        p2.start()

        self.assertRaises(DataMatchedException)


if __name__ == '__main__':
    unittest.main()
