from django.contrib import admin
from.models import *
# Register your models here.
class AllAdmin(admin.ModelAdmin):
    readonly_fields = ('codigo',)

admin.site.register(modalidad,AllAdmin)
admin.site.register(oferta,AllAdmin)