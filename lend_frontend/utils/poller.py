from heat_client_helper import HeatClientHelper

class Poller(object):
    def __init__(self, **kwargs):
        self.heat_helper = HeatClientHelper(**kwargs)
        self.heat_client = self.heat_helper.get_client()

    def start(self):

        def send_mail(**kwargs):
            print 'to do mail'

            clean_dict[o['output_key']] = {
                'description': o['description'],
                'value': o['output_value']
            }

        return clean_dict

    for stack in stacks:
        full_stack = heat_client.stacks.get(stack.id)
        template_outputs = full_stack.outputs
        clean_output = outputs
        stacks = self.heat_helper.get_completed_stacks()

        from time import sleep

        for stack in stacks:
            full_stack = self.heat_client.stacks.get(stack.id)
            template_outputs = full_stack.outputs
            clean_output = outputs_transform(template_outputs)
            # To cst
            if 'm_notification_status' in clean_output and not clean_output['m_notification_status']['value']:
                template = heat_client.stacks.template(stack.id)

                parameters = parameters_clean(full_stack.parameters)
                parameters['notification_status'] = True

                fields = {
                    'stack_name': stack.stack_name,
                    'disable_rollback': True,
                    'template': template,
                    'parameters': parameters,
                }

                stack.update(**fields)
                send_mail()

    def outputs_transform(self, outputs):
        clean_dict = {}
        for o in outputs:
            clean_dict[o['output_key']] = {
                'description': o['description'],
                'value': o['output_value']
            }

        return clean_dict

    def parameters_clean(self, stack_parameters):
        parameters = {}
        for key in stack_parameters:
            if not key.startswith('AWS::'):
                parameters[key] = stack_parameters[key]

        return parameters

if __name__ == "__main__":
    kwargs = {
        'auth_url': 'http://10.31.92.131:5000/v2.0',
        'tenant_name': 'OS-Lend',
        'username': 'a.cavat',
        'password': 'CecoojEg8'
    }



    def get_stack_outputs(stack_id):
        return 

    def stack_update():
        print 'to do update'

    def send_mail(**kwargs):
        print 'to do mail'

    htch = HeatClientHelper(**kwargs)
    heat_client = htch.get_client()
    stacks = htch.get_completed_stacks()

    from time import sleep

    # template = heat_client.stacks.get(stacks[0].id)

    def outputs_transform(outputs):
        clean_dict = {}
        for o in outputs:
            clean_dict[o['output_key']] = {
                'description': o['description'],
                'value': o['output_value']
            }

        return clean_dict

    for stack in stacks:
        full_stack = heat_client.stacks.get(stack.id)
        template_outputs = full_stack.outputs
        clean_output = outputs_transform(template_outputs)
        # To cst
        if 'm_notification_status' in clean_output and not clean_output['m_notification_status']['value']:
            template = heat_client.stacks.template(stack.id)

            parameters = {}
            for key in full_stack.parameters:
                if not key.startswith('AWS::'):
                    parameters[key] = full_stack.parameters[key]
            print parameters

            parameters['notification_status'] = True

            fields = {
                'stack_name': stack.stack_name,
                'disable_rollback': True,
                'template': template,
                'parameters': parameters,
            }

            stack.update(**fields)
            send_mail()

