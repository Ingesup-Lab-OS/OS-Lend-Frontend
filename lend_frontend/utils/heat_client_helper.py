from heatclient import client as heat_client
from keystone_helper import KeystoneHelper

class HeatClientHelper(object):
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

    def get_completed_stacks(self):
        #FIXME This shit doesn't work
        #stacks = self.client.stacks.list(filters={'stack_status': 'CREATE_COMPLETE'})
        stacks = self.client.stacks.list()
        created_stacks = []
        for stack in stacks:
            if stack.status == 'COMPLETE':
                created_stacks.append(stack)
        return created_stacks

    def stack_exists(self, stack_name):
        try:
            self.client.stacks.get(stack_name)
        except:
            return False
            
        return True

if __name__ == "__main__":
    kwargs = {
        'auth_url': 'http://10.31.92.131:5000/v2.0',
        'tenant_name': 'OS-Lend',
        'username': 'a.cavat',
        'password': 'CecoojEg8'
    }
