from django.contrib import admin
from Apply.models import Etudiant, Candidature,Annee
import watson

class EtudiantAdmin(watson.SearchAdmin, admin.ModelAdmin):
	list_display   = ('id', 'nom', 'prenom', 'email')
	ordering       = ('nom','prenom')
	search_fields = ('nom','prenom','email')

admin.site.register(Etudiant, EtudiantAdmin)

class CandidatureAdmin(watson.SearchAdmin, admin.ModelAdmin):
	list_display = ('etudiant','date_demande','demande','reponse','confirmation')
	search_fields = ("confirmation","date_demande")

admin.site.register(Candidature, CandidatureAdmin)


class AnneeAdmin(admin.ModelAdmin):
	list_display = ('etudiant','millesime','etablissement','formation','resultat')
	
admin.site.register(Annee, AnneeAdmin)




