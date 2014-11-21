from heatclient import client as heat_client
from keystone_helper import KeystoneHelper

class HeatClientHelper:
    DEFAULT_VERSION = '1'

    def __init__(self, **kwargs):
        self.keystone_client = KeystoneHelper(**kwargs)
        endpoint = self.keystone_client.get_endpoint()
        _version = kwargs['version'] if 'version' in kwargs else self.DEFAULT_VERSION
        token = self.keystone_client.get_token()
        kwargs.update({'token': token})
        self.client = heat_client.Client(_version, endpoint, **kwargs)

    def get_client(self):
        return self.client

    def stack_exists(self, stack_name):
        try:
            hc.stacks.get(stack_name)
        except:
            return False
            
        return True