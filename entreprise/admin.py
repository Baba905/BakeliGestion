from django.contrib import admin
from entreprise.models import Entreprise
class EntrepriseAdmin(admin.ModelAdmin):
    pass

admin.site.register(Entreprise, EntrepriseAdmin)
