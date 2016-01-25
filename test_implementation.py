__author__ = 'Kanyu'

#import nosetest
import unittest
from implementscrape import *


class TestImpl(unittest.TestCase):

    def setUp(self):
        pass

    def testConnection(self):
        bill = Testor()
        self.assertEqual(bill.connectionmade(),True)


if __name__ == '__main__':
    Testor()
