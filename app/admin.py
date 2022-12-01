from django.contrib import admin
from .models import User,LoginLogs,Car,BookingRequest
from django.contrib.auth.admin import UserAdmin as BaseAdmin
# Register your models here.
class UserAdmin(BaseAdmin):
    # The forms to add and change user instances


    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('id','username','email', 'user_type', 'is_admin','is_staff')
    list_filter = ('is_admin',)
    fieldsets = (
        ('User Credentials', {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email','user_type')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'user_type', 'password1', 'password2'),
        }),
    )
    search_fields = ('id','email')
    ordering = ('email',)
    filter_horizontal = ()
admin.site.register(User, UserAdmin)

@admin.register(LoginLogs)
class LoginLogAdmin(admin.ModelAdmin):
    list_display=["id","user","user_type","login_at"]

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display=["id","car_model","colour","fuel_type","car_images","is_available","owner"]

@admin.register(BookingRequest)
class CarAdmin(admin.ModelAdmin): 
    list_display=["id","requested_by","requested_to","requested_for","request_status","created_on","modified_on"]