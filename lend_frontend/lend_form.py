# coding=utf-8

from django import forms
import datetime

class LendForm(forms.Form):
    projectName = forms.CharField(label='Nom du projet', 
        error_messages={'required': 'Le nom du projet est requis'})
    description = forms.CharField(label='Déscription', required=False)
    mail = forms.EmailField(label='Email',
        error_messages={'required': 'Votre adresse mail est requise'})
    sshKey = forms.CharField(label='Clé SSH' )
    validity = forms.DateField(label='Validité', 
        initial=datetime.date.today, input_formats='%d/%m/%y',
        error_messages={'required': 'Veuillez selectionner une date'})
    description = forms.CharField(required=False)
    # Todo
    # flavor = forms.ModelChoiceField(queryset={ 1: 'a', 2: 'b'}, empty_label=None)
    # heatTemplate = forms.ModelChoiceField(queryset={ 1: 'a', 2: 'b'}, empty_label=None)