from django import forms
from .models import Employee
class EmployeeForm(forms.ModelForm):

    class Meta:
        model=Employee
        fields='__all__'

    def __init__(self,*args,**kwargs):
        super(EmployeeForm,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label="Select"
        self.fields['job'].empty_label="Select"
        self.fields['state'].empty_label="Select"
        self.fields['city'].empty_label="Select"