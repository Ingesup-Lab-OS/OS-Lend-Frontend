from keystoneclient.v2_0 import client

class KeystoneHelper:

    def __init__(self, **kwargs):
        self.client = client.Client(**kwargs)
        self.endpoint = self.client.service_catalog.url_for(
            service_type= 'orchestration',
            endpoint_type= 'publicURL'
        )
        self.token = self.client.auth_token

    def get_client(self):
        return self.client

    def get_endpoint(self):
        return self.endpoint

    def get_token(self):
        return self.token