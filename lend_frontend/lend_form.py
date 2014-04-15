# coding=utf-8

from django import forms
from django.conf import settings
from utils.heat_template_helper import HeatTemplateHelper
from libs.nova_flavor_provider import NovaFlavorProvider
import datetime

class LendForm(forms.Form):

    project_name = forms.CharField(label='Nom du projet', 
        error_messages={'required': 'Le nom du projet est requis'})
    
    description = forms.CharField(label='Déscription', required=False)
    
    mail = forms.EmailField(label='Email',
        error_messages={'required': 'Votre adresse mail est requise'})
    
    ssh_key = forms.CharField(label='Clé SSH' )
    
    validity = forms.DateField(label='Validité', 
        initial=datetime.date.today, 
        input_formats=['%d/%m/%y'],
        error_messages={'required': 'Veuillez selectionner une date'})

    nova_flavor = NovaFlavorProvider().get_flavors_list()
    flavor = forms.ChoiceField(nova_flavor, label='Capacité', widget=forms.Select(attrs={'class':'form-control'}))

    heat_path = "%s/%s" %(settings.BASE_DIR, settings.HEAT_TEMPLATE_NAME)
    heat_templates_tuple = HeatTemplateHelper.get_all_tuples_from_path("%s/heat/" % heat_path)
    heat_template = forms.ChoiceField(heat_templates_tuple, label='Template', widget=forms.Select(attrs={'class':'form-control'}))