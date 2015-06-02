from django import forms
from .models import *

class EtudiantForm(forms.ModelForm):
	class Meta:
		model = Etudiant
		fields = '__all__'


class CandidatureForm(forms.ModelForm):
	class Meta:
		model = Candidature
		fields = '__all__'

class PortailForm(forms.ModelForm):
	class Meta:
		model = Etudiant
		fields =('nom', 'prenom')