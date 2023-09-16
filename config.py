
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/service')
print(os.path.dirname(os.path.abspath(__file__)) + '/service')

from service.swagger_client.configuration import Configuration
from service.swagger_client.api_client import ApiClient

class AppConfiguration(Configuration):
    def __init__(self, host="http://localhost:8000/api"):
        super().__init__()
        self.host = host
