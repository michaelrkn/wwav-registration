from django.contrib import admin

# Register your models here.
from core.models import Registration, Mail, Zip

admin.site.register(Mail)
admin.site.register(Registration)
admin.site.register(Zip)
