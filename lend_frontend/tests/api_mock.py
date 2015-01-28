import datetime


class FakeHeatTemplateManager(object):
    def __init__(self):
        self.templates = {
            1: 'Dummy description #1.',
            3: 'Dummy description #3.',
            4: 'Dummy description #4.',
            6: 'Dummy description #6.'}

    def get_description(self, template_id):
        return self.templates[template_id]

    def list_templates(self):
        return self.templates.keys()


class FakeNovaAPI(object):
    def __init__(self):
        self.flavors = {
            1: {
                'name': 'flavor1', },
            2: {
                'name': 'flavor2', }}

    def get_flavor(self, flavor_id):
        return self.flavors[flavor_id]

    def list_flavors(self):
        return self.flavors.keys()


class FakeHeatAPI(object):
    def __init__(self):
        self.stacks = {
            'stack1': {
                'email': 'dummy1@localhost', },
            'stack2': {
                'email': 'dummy2@localhost', }}

        self.expired_stacks = {
            'stack3': {
                'email': 'dummy3@localhost', }}

    def create_stack(self, name, template_id, **params):
        # TODO(sheeprine): Implement checks
        if name in self.stacks or name in self.expired_stacks:
            return False
        self.stacks[name] = params
        return True

    def delete_stack(self, name):
        if name is self.stacks:
            self.stacks.pop(name)
            return True
        else:
            return False

    def expired_stacks(self):
        return ['stack1', 'stack2']

    def disable_expired_stacks(self):
        return len(self.expired_stacks)

    def purge_expired_stacks(self):
        purged = len(self.expired_stacks)
        self.expired_stacks = {}
        return purged

    def extend_stack_validity(self, name, days):
        if name in self.expired_stacks:
            return datetime.datetime.utcnow()

    def list_new_stacks(self):
        return ['stack4']

    def get_stack_details(self, name):
        return self.stacks[name]
