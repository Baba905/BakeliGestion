from django.contrib import admin
from bakeliGestion.models import Eleve,Entreprise,Offre,Etablissement#,Postuler

class EleveAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'niveau')

class EntrepriseAdmin(admin.ModelAdmin):
    list_display = ('nom', 'adresse')

class OffreAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date')

class EtablissementAdmin(admin.ModelAdmin):
    list_display = ('nom', 'adresse')

class PostulerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Etablissement,EtablissementAdmin)
admin.site.register(Eleve,EleveAdmin)
admin.site.register(Entreprise,EntrepriseAdmin)
admin.site.register(Offre,OffreAdmin)
#admin.site.register(Postuler,PostulerAdmin)