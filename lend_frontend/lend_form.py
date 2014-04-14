# coding=utf-8

from django import forms
from django.conf import settings
from utils.heat_template_helper import HeatTemplateHelper
from libs.nova_flavor_provider import NovaFlavorProvider
import datetime

class LendForm(forms.Form):

    projectName = forms.CharField(label='Nom du projet', 
        error_messages={'required': 'Le nom du projet est requis'})
    
    description = forms.CharField(label='Déscription', required=False)
    
    mail = forms.EmailField(label='Email',
        error_messages={'required': 'Votre adresse mail est requise'})
    
    sshKey = forms.CharField(label='Clé SSH' )
    
    validity = forms.DateField(label='Validité', 
        initial=datetime.date.today, 
        input_formats=['%d/%m/%y'],
        error_messages={'required': 'Veuillez selectionner une date'})
    
    description = forms.CharField(required=False)
    
    nova_flavour = NovaFlavorProvider().get_flavors_list()
    flavor = forms.ChoiceField(nova_flavour, label='Puissance')
    
    heat_path = "%s/%s" %(settings.BASE_DIR, settings.HEAT_TEMPLATE_NAME)
    heat_templates = HeatTemplateHelper.get_all_tuples_from_path("%s/heat/" % heat_path)
    heatTemplate = forms.ChoiceField(heat_templates, label='Template')