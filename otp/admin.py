from django.contrib import admin
from .models import OTP

# Register your models here.
class OTPAdmin(admin.ModelAdmin):
    list_display = ['email','otp','OTPGenerated_at']

admin.site.register(OTP,OTPAdmin)