import unittest
from connectmp import Connection
import multiprocessing as mp
from tests.funcs import do_something, track_i
from tests.exceptions import DataMatchedException


class TestConnectMP(unittest.TestCase):

    def test_connection(self):
        data = "Crabby Patty's Secret Formula!"

        connection = Connection()

        p1 = mp.Process(target=do_something, args=(connection, data))
        p2 = mp.Process(target=track_i, args=(connection, data))

        p1.start()
        p2.start()

        self.assertRaises(DataMatchedException)


if __name__ == '__main__':
    unittest.main()
