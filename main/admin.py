from django.contrib import admin
from .models import WebsiteModel, FailedWebsiteModel

# Register your models here.
admin.site.register(WebsiteModel)
admin.site.register(FailedWebsiteModel)
