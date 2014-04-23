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

if __name__ == "__main__":
    kc_args = {
        'auth_url': 'http://10.31.92.131:5000/v2.0',
        'tenant_name': 'OS-Lend',
        'username': 'a.cavat',
        'password': 'CecoojEg8'
    }
    print KeystoneHelper(**kc_args).get_token()