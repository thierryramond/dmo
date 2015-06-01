from django.contrib import admin
from Apply.models import Etudiant, Candidature,Annee

class EtudiantAdmin(admin.ModelAdmin):
	list_display   = ('id', 'nom', 'prenom', 'email')
	ordering       = ('nom','prenom')

admin.site.register(Etudiant, EtudiantAdmin)

class CandidatureAdmin(admin.ModelAdmin):
	list_display = ('etudiant','date_demande','demande','reponse','confirmation')

admin.site.register(Candidature, CandidatureAdmin)


class AnneeAdmin(admin.ModelAdmin):
	list_display = ('etudiant','millesime','etablissement','formation','resultat')
	
admin.site.register(Annee,AnneeAdmin)