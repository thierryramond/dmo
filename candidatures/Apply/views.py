from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView, FormView

from Apply.models import Etudiant, Candidature
from Apply.forms import EtudiantForm, CandidatureForm

#-----------------------------------------------------------------------------
#  index

def home(request):
	return render(request,'Apply/home.html',{'datetime': timezone.now()})


#-----------------------------------------------------------------------------
#  search Etudiant


### A FAIRE!


#-----------------------------------------------------------------------------
#  Etudiant list

class EtudiantListView(ListView):
	model = Etudiant
	template_name = 'Apply/etudiant_list.html'
	ordering = ('nom','prenom')

#-----------------------------------------------------------------------------
#  Etudiant create

class EtudiantCreateView(CreateView):
	template_name = 'Apply/etudiant_edit.html'
	form_class  = EtudiantForm
	success_url = reverse_lazy('etudiant_list')

	def form_valid(self,form):
		etudiant = Etudiant(
			genre = form.cleaned_data['genre'],
			nom = form.cleaned_data['nom'],
			prenom = form.cleaned_data['prenom'],
    		date_naissance =  form.cleaned_data['date_naissance'],
    		adresse = form.cleaned_data['adresse'],
    		email = form.cleaned_data['email'],
    		vient_de = form.cleaned_data['vient_de'],
			)
		etudiant.save()

		return HttpResponseRedirect(reverse_lazy('etudiant_list'))


#-----------------------------------------------------------------------------
#  Etudiant delete

class EtudiantDeleteView(DeleteView):
	model = Etudiant
	template_name = 'Apply/etudiant_delete.html'

	def get_success_url(self):
		return reverse_lazy('etudiant_list')

#-----------------------------------------------------------------------------
#  Etudiant update

class EtudiantUpdateView(UpdateView):
	model = Etudiant
	template_name = 'Apply/etudiant_edit.html'
	form_class = EtudiantForm

	def get_success_url(self):
		return reverse('etudiant_list')

	def get_context_data(self, **kwargs):
		context = super(EtudiantUpdateView, self).get_context_data(**kwargs)
		context['action'] = reverse('etudiant_edit', kwargs={'pk': self.get_object().id})
		return context

#-----------------------------------------------------------------------------
#  Etudiant detail

class EtudiantView(DetailView):

	model = Etudiant
	template_name = 'Apply/etudiant.html'


#-----------------------------------------------------------------------------
#  Candidature List 

class CandidatureListView(ListView):
	model = Candidature
	template_name = 'Apply/candidature_list.html'
	ordering = ('date_demande')
		

#-----------------------------------------------------------------------------
# Candidature detail


class CandidatureView(DetailView):

	model = Candidature
	template_name = 'Apply/candidature.html'

#-----------------------------------------------------------------------------
#  Candidature create


class CandidatureCreateView(CreateView):
	template_name = 'Apply/candidature_edit.html'
	form_class  = CandidatureForm
	success_url = reverse_lazy('candidature_list')

	def form_valid(self,form):
		candidature = Candidature(
			etudiant = form.cleaned_data['etudiant'],
			date_demande= form.cleaned_data['date_demande'],
			demande = form.cleaned_data['demande'],
    		reponse =  form.cleaned_data['reponse'],
    		confirmation = form.cleaned_data['confirmation'],
    		reponse_donnee_par = form.cleaned_data['reponse_donnee_par'],
    		date_reponse= form.cleaned_data['date_reponse'],
			)
		etudiant.save()

		return HttpResponseRedirect(reverse_lazy('candidature_list'))


