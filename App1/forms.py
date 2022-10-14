from django import forms
from .models import Student
class Formclass(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','age','mark1','mark2','mark3',]
        # exclude = ['name','age','mark1','mark2','mark3','total','avg','grade']
        # widgets = {
        #     'name':forms.TextInput(attrs={'class':'form-control'}),
        #     'age':forms.NumberInput(attrs={'class':'form-control'}),
        #     'mark1':forms.NumberInput(attrs={'class':'form-control'}),
        #     'mark2':forms.NumberInput(attrs={'class':'form-control'}),
        #     'mark3':forms.NumberInput(attrs={'class':'form-control'}),
        #     'total':forms.NumberInput(attrs={'class':'form-control'}),
        #     'avg':forms.NumberInput(attrs={'class':'form-control'}),
        #     'grade':forms.TextInput(attrs={'class':'form-control'}),
        # }