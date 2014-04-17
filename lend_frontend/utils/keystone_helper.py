from keystoneclient.v2_0 import client

class KeystoneHelper:
    @staticmethod
    def get_endpoint(**kwargs):
        ksclient = client.Client(**kc_args)
        return ksclient.service_catalog.url_for(
            service_type= 'orchestration',
            endpoint_type= 'publicURL'
        )

if __name__ == "__main__":
    kc_args = {
        'auth_url': 'http://10.31.92.131:5000/v2.0',
        'tenant_name': 'OS-Lend',
        'username': 'a.cavat',
        'password': 'CecoojEg8'
    }
    print KeystoneHelper.get_endpoint(**kc_args)