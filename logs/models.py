from django.db import models
from django import forms

class NameForm(forms.Form):
    domain = forms.URLField(label='domain', required=False)
    logs = forms.CharField(label='logs', max_length=100)

class Logs(models.Model):
    domain = models.CharField(max_length=50)
    text_log = models.CharField(max_length=10000)
    date_add = models.DateTimeField()
    type_logs = models.CharField(max_length=50)

    class Meta:
        db_table = 'domain_logs'