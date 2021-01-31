from django.contrib import admin
from .models import Account

# Register your models here.
class AccountManager(admin.ModelAdmin):
    list_display = ('email','mobile_no','first_name','last_name')

admin.site.register(Account,AccountManager)


