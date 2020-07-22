import unittest
from back.config import Config
from back.utils.validators import validator_mail
import time

class TestLoad(unittest.TestCase):
    """si es menor de 1 seg, es correcta.  self.assertLess(time_lapsed,1) """
    def test_load(self):
        start = time.time()
        mail = validator_mail("Carlosr@hotmail.com")
        end = time.time()
        time_lapsed = end - start
        self.assertLess(time_lapsed,1) 
