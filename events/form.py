from django import forms
from .models import Event

class CreateEventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ('status','admin_comment','date_created','user')

class EventAdminResponseForm(forms.ModelForm):
    class Meta:
        model = Event
        fields =['status','admin_comment']
