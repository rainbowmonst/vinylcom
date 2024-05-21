# В файле forms.py вашего приложения
from django import forms

class OrderForm(forms.Form):
    card_number = forms.CharField(label='Enter your card number', max_length=16)
    cvv = forms.CharField(label='Enter the CVV code', max_length=3)