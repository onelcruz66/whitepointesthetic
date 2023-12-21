from django import forms
from whitepointapp.models import RequestAppointment, MessageRequest

class RequestForm(forms.ModelForm): 
    class Meta:
        model = RequestAppointment
        fields = ['first_name', 'last_name', 'email_address', 'phone_number','service', 'date', 'time']

        service = forms.ChoiceField(choices=[('Massage', 'Massage'), ('Waxing', 'Waxing'), ('Skincare', 'Skincare')])

class MessageForm(forms.ModelForm):
    class Meta:
        model = MessageRequest
        fields = ['full_name', 'email_address', 'phone_number','service', 'text_content']

        service = forms.ChoiceField(choices=[('Massage', 'Massage'), ('Waxing', 'Waxing'), ('Skincare', 'Skincare'), ('Other', 'Other')])