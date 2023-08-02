import unittest

suit = unittest.defaultTestLoader.discover(r'C:\Users\yuemia\PycharmProjects\test_guo\test_func')
runer = unittest.TextTestRunner()
runer.run(suit)
