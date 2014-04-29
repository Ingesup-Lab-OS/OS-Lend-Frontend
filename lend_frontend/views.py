from django.shortcuts import render
from .lend_form import LendForm
from libs.nova_flavor_provider import NovaFlavorProvider
from utils.heat_template_fetcher import HeatTemplateFetcher
from django.http import Http404, HttpResponse
from django.utils.html import strip_tags
from heatclient.common import template_utils
from utils.heat_template_helper import HeatTemplateHelper
import json

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

    else:
        form = LendForm()

    return render(request, 'index.html', {
        'form': form,
    })

def flavor(request, id=0):
    if id != 0 or request.is_ajax():
        id = strip_tags(id)
        flavor = NovaFlavorProvider().get_flavour_by_id(id)
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
