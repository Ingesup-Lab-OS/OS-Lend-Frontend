from novaclient.v1_1 import client

class NovaClientHelper:
    def __init__(self, **kwargs):
        self.client = client.Client(
            kwargs['username'],
            kwargs['password'],
            kwargs['tenant_name'],
            kwargs['auth_url'],
            service_type="compute"
        )

    def get_flavors_list(self):
        flavors =  self.client.flavors.list()
        l = []
        for f in flavors:
            l.append(self.get_tuple_from_flavor(f))

        return tuple(l)

    def get_tuple_from_flavor(self, flavour):
        return (flavour.id, flavour.name)

    def get_flavour_by_id(self, id):
        return self.client.flavors.get(id)

    def get_client(self):
        return self.client

    def keypair_create(self, keypair_name):
        from novaclient import exceptions
        def create(keypair_name):
            return self.client.keypairs.create(keypair_name)

        def delete(keypair_name):
            return self.client.keypairs.delete(keypair_name)

        try:
            return create(keypair_name)
        except exceptions.Conflict as e:
            delete(keypair_name)
            return create(keypair_name)