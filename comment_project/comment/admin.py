from django.contrib import admin
from .models import ContactUs
from django.core.exceptions import ValidationError

# Register your models here.


class contactAdmin(admin.ModelAdmin):
    list_display = ("Fullname" , "Email")
    def formfield_for_dbfield(self, db_field, **kwargs):
        formsfield=super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name=="Fullname":
            formsfield.validators.append(self.checkEmpty)
        return formsfield
    def checkEmpty(self,value):
        if len(value)==1 or len(value)==2:
            raise ValidationError("تعداد کارکتر مجاز نیست!")
        if len(value)==20:
            raise ValidationError("تعداد کارکتر مجاز نیست!")









admin.site.register(ContactUs , contactAdmin)
