from django.contrib import admin
from eleve.models import Eleve

class EleveAdmin(admin.ModelAdmin):
    pass

admin.site.register(Eleve,EleveAdmin)
