class NovaFlavorProvider:
    def __init__(self):
        from novaclient.v1_1 import client
        self.client = client.Client(
            'a.cavat', 
            'CecoojEg8', 
            'OS-Lend', 
            'http://10.31.92.131:5000/v2.0', 
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


if __name__ == "__main__":
    from novaclient.v1_1 import client
    nt = client.Client(
        'a.cavat', 
        'CecoojEg8', 
        'OS-Lend', 
        'http://10.31.92.131:5000/v2.0', 
        service_type="compute"
    )
    flavors =  nt.flavors.list()