from django.contrib import admin
from .models import SFTask, SFOutward, SFInward

# Register your models here.
admin.site.register(SFTask)
admin.site.register(SFOutward)
admin.site.register(SFInward)
