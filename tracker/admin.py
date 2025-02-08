from django.contrib import admin
from django.contrib.admin import register
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from import_export.admin import ImportExportModelAdmin
from unfold.admin import ModelAdmin
from unfold.contrib.filters.admin import RangeDateFilter, SliderNumericFilter
from unfold.contrib.import_export.forms import (ExportForm, ImportForm)
from unfold.forms import (AdminPasswordChangeForm, UserChangeForm,
                          UserCreationForm)

from .models import Link

# Register your models here
admin.site.unregister(User)

class CustomeSliderNumericFilter(SliderNumericFilter):
    MAX_DECIMALS = 2
    STEP = 10


@register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm


class LinkAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ['id', 'name', 'url', 'current_price', 'old_price', 'price_difference']
    import_form_class = ImportForm
    export_form_class = ExportForm
    list_filter = [
        ('created', RangeDateFilter),
        ('current_price', CustomeSliderNumericFilter),
        
    ]
    
    list_filter_submit = True # submit button at the bottom of the filter
    

admin.site.register(Link, LinkAdmin)