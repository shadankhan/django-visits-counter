from django.contrib import admin
from visits_counter.models import Visit

class VisitAdmin(admin.ModelAdmin):
    pass

admin.site.register(Visit, VisitAdmin)
