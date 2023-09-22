from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _    #while importing method/file/class we can replace name as other '_'

User=get_user_model() #django automatically imports our custome user model by using this method

    
class UserAdmin(UserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'fullname', 'date_joined')
    list_filter = ('is_superuser', 'is_active')
    search_fields = ('email',)  #if there is a single element in tuple a comma "," is needed after the element
    ordering = ('email',)   #if there is a single element in tuple a comma "," is needed after the element
 
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('fullname',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'fullname'),
        }),
    )
 
 
admin.site.register(User, UserAdmin)

