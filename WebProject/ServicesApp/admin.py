from django.contrib import admin
from .models import Service

# Model registration

class ServiceAdmin(admin.ModelAdmin):
    readonly_fields=('createdAt', 'updatedAt') # Specify only for reading

admin.site.register(Service, ServiceAdmin)