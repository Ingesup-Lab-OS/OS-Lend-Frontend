from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.utils.html import strip_tags
from django.conf import settings

from .lend_form import LendForm
from heatclient.common import template_utils
import json

from utils.nova_client_helper import NovaClientHelper
from utils.heat_template_fetcher import HeatTemplateFetcher
from utils.heat_template_helper import HeatTemplateHelper
from utils.heat_client_helper import HeatClientHelper

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = LendForm(request.POST)
        if form.is_valid():
            project_name = form.cleaned_data['project_name']
            mail = form.cleaned_data['mail']
            ssh_key = form.cleaned_data['ssh_key']
            validity = form.cleaned_data['validity']
            description = form.cleaned_data['description']
            flavor = form.cleaned_data['flavor']

            template_id = form.cleaned_data['heat_template']
            template_path = HeatTemplateHelper.get_full_path_from_file_name(template_id)
            tpl_files, template_content = template_utils.get_template_contents(template_path)

            kp = NovaClientHelper(**settings.OS_PARAMS).keypair_create(project_name)

            parameters = {
                'f_name': flavor,
                'kp_name': project_name,
                'img_name': 'Ubuntu precise',
                'subnet_id': settings.SUBNET_ID,
                'net_id': settings.NET_ID,
                'floating_id': settings.FLOATING_ID,
                'description': description,
                'mail': mail,
                'validity': validity.isoformat(),
                'notification_status': False,
            }

            fields = {
                'stack_name': project_name,
                'disable_rollback': True,
                'template': template_content,
                'parameters': parameters,
            }

            _htc = HeatClientHelper(**settings.OS_PARAMS).get_client()
            hc = _htc.stacks.create(**fields)

            from django.contrib import messages
            messages.add_message(request, messages.SUCCESS, 'Well done.')
            # astack = _htc.stacks.get(testor['id'])
            # stacks = HeatClientHelper(**settings.OS_PARAMS).get_completed_stacks()
            # while not stacks:
            #     from time import sleep
            #     sleep(1)
            #     stacks = HeatClientHelper(**settings.OS_PARAMS).get_completed_stacks()
            
            # astack = stacks[0]
            # fields['parameters']['mail'] = 'fjkdfjmfkjds'
            # astack.update(**fields)


    else:
        form = LendForm()

    return render(request, 'index.html', {
        'form': form,
    })

def flavor(request, id=0):
    if id != 0 or request.is_ajax():
        id = strip_tags(id)
        flavor = NovaClientHelper(**settings.OS_PARAMS).get_flavour_by_id(id)
        dic = {
            'id': flavor.id,
            'name': flavor.name,
            'ram': flavor.ram,
            'disk': flavor.disk,
            'vcpus': flavor.vcpus
        }
        return HttpResponse(json.dumps(dic), mimetype='application/json')

    raise Http404

def heat_template(request, id=0):
    if id != 0 or request.is_ajax():
        id = strip_tags(id)
        htf = HeatTemplateFetcher()
        yaml_file = htf.get_yaml_file_path_from_name(id)
        yaml_dic = htf.get_yaml(yaml_file)
        description = htf.get_description_from_yaml(yaml_dic)
        dic = {
            'description': description
        }
        return HttpResponse(json.dumps(dic), mimetype='application/json')

    raise Http404
