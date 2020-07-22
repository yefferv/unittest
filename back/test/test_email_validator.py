import unittest
from back.config import Config
from back.utils.validators import validator_mail
import time

class TestEmailValidator(unittest.TestCase):
    """Testing email"""
    def test_email_validator(self):
        self.assertTrue(validator_mail("Carlosr@hotmail.com"))
