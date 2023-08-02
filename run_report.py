import unittest
from unittestreport import TestRunner
suit=unittest.defaultTestLoader.discover(r"C:\Users\yuemia\PycharmProjects\test_guo\test_func")
runner=TestRunner(suit)
runner.run()


