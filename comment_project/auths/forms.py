from django import forms






class LOIGIN(forms.Form):
    def __init__(self,*args,**kwargs):
        super(LOIGIN,self).__init__(*args,**kwargs)
        for item in LOIGIN.visible_fields(self):
             item.field.widget.attrs["class"]="form-control"

    email=forms.CharField(max_length=200,template_name="Email")
    password=forms.CharField(max_length=255,template_name="Password")

class Register(forms.Form):
    def __init__(self, *args, **kwargs):
        super(Register, self).__init__(*args, **kwargs)
        for item in Register.visible_fields(self):
            item.field.widget.attrs["class"] = "form-control"

    Name = forms.CharField(max_length=200, template_name="Name")
    Email = forms.CharField(max_length=200, template_name="Email")
    Password = forms.CharField(max_length=255, template_name="Password")