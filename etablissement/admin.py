from django.contrib import admin
from etablissement.models import Etablissement

class EtablissementAdmin(admin.ModelAdmin):
    pass

admin.site.register(Etablissement,EtablissementAdmin)
