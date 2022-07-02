from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import User
# Register your models here.

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'date_of_birth', 'is_admin', 'nickname',)
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields':('email','password')}),
        ('Personal info',{'fields':('date_of_birth',)}),
        ('Permissions',{'fields':('is_admin',)}),
    )
    list_display_links = ('nickname', 'email',)

    add_fieldset = (
        (None, {
            'classes':('wide',),
            'fields':('email','date_of_birth','password1','password2', 'nickname',)
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)