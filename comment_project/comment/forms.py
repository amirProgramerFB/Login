from django import forms
from .models import ContactUs


class contactusModel(forms.Form):
    def __init__(self,*args,**kwargs):
        super(contactusModel,self).__init__(*args,**kwargs)
        for item in contactusModel.visible_fields(self):
             item.field.widget.attrs["class"]="form-control"


    Fullname=forms.CharField(required=True,max_length=200,label="نام کامل")
    Email=forms.CharField(required=True,label="ایمیل",widget=forms.EmailInput)
    message=forms.CharField(widget=forms.Textarea,label="پیام")
    Id=forms.CharField(widget=forms.HiddenInput ,required=True)

"""
class contactusModel(forms.ModelForm):
    class Meta:
        model=ContactUs
        fields="__all__"
"""