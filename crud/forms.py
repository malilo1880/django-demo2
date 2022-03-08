from django import forms
from crud.models import Registration


class Reg_form(forms.ModelForm):
      class Meta:
            model=Registration
            fields ='__all__'