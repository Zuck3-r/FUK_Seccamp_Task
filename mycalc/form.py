from django import forms

class numForm(forms.Form):
  a = forms.DecimalField(label='num1', initial=2, required=True)
  b = forms.DecimalField(label='num2', initial=1, required=True)