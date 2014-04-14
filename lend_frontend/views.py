from django.shortcuts import render
from .lend_form import LendForm
from libs.nova_flavor_provider import NovaFlavorProvider
from django.http import Http404, HttpResponse
import json

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = LendForm(request.POST)
    else:
        form = LendForm()

    return render(request, 'index.html', {
        'form': form,
    })

def flavor(request, id=0):
    if id != 0 or request.is_ajax():
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
        dic = {
            'description': id
        }
        return HttpResponse(json.dumps(dic), mimetype='application/json')

    raise Http404