# coding=utf-8

from django import forms
from django.conf import settings
from utils.heat_template_helper import HeatTemplateHelper
from utils.nova_client_helper import NovaClientHelper
from utils.heat_client_helper import HeatClientHelper
import datetime
from django.core.exceptions import ValidationError

def validate_stack_name_exists(value):
    hch = HeatClientHelper(**settings.OS_PARAMS)
    if(hch.stack_exists(value)):
        raise ValidationError('Un projet portant ce nom existe déjà.')
    
class LendForm(forms.Form):

    project_name = forms.CharField(label='Nom du projet', 
        error_messages={'required': 'Le nom du projet est requis'},
        validators=[validate_stack_name_exists])
    
    description = forms.CharField(label='Description', required=False)
    
    mail = forms.EmailField(label='Email',
        error_messages={'required': 'Votre adresse mail est requise'})
    
    ssh_key = forms.CharField(label='Clé SSH', required=False)
    
    validity = forms.DateField(label='Validité', 
        input_formats=['%Y-%m-%d', '%d/%m/%Y', '%d/%m/%Y'],
        error_messages={'required': 'Veuillez selectionner une date'})

    nova_flavor = NovaClientHelper(**settings.OS_PARAMS).get_flavors_list()
    flavor = forms.ChoiceField(nova_flavor, label='Capacité', widget=forms.Select(attrs={'class':'form-control'}))

    heat_path = "%s/%s" %(settings.BASE_DIR, settings.HEAT_TEMPLATE_NAME)
    heat_templates_tuple = HeatTemplateHelper.get_all_tuples_from_path("%s/heat/" % heat_path)
    heat_template = forms.ChoiceField(heat_templates_tuple, label='Template', widget=forms.Select(attrs={'class':'form-control'}))