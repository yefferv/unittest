from flask_testing import TestCase
from back.config import config
from back.models import create_app

enviroment = config['development']
app = create_app(enviroment)

class BaseTestCase(TestCase):
    def create_app(self):
        return app

