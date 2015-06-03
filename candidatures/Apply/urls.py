from django.conf.urls import include, url
from Apply import views
from Apply.views import EtudiantListView

urlpatterns = [
    url(r'^$', 'Apply.views.home', name= 'home'),
    url(r'^index/$', 'Apply.views.home', name= 'home'),
    url(r'^home/$', 'Apply.views.home', name= 'home'),
    
    url(r'^list/$', views.EtudiantListView.as_view(), name= 'etudiant_list'),
    url(r'^new/$', views.EtudiantCreateView.as_view(), name= 'etudiant_new'),
	url(r'^delete/(?P<pk>\d+)/$', views.EtudiantDeleteView.as_view(), name= 'etudiant_delete'),
	url(r'^edit/(?P<pk>\d+)/$', views.EtudiantUpdateView.as_view(), name='etudiant_edit',),
	url(r'^(?P<pk>\d+)/$', views.EtudiantView.as_view(), name='etudiant_detail',),
	url(r'^etudiant_search/$', views.EtudiantPortailView.as_view(), name='etudiant_search',),

	url(r'^candidature_list/$', views.CandidatureListView.as_view(), name= 'candidature_list'),
	url(r'^candidature/(?P<pk>\d+)/$', views.CandidatureView.as_view(), name='candidature_detail',),
	url(r'^candidature_new/$', views.CandidatureCreateView.as_view(), name= 'candidature_new'),
	url(r'^candidature_edit/(?P<pk>\d+)/$', views.CandidatureUpdateView.as_view(), name='candidature_edit',),


	url(r"^search/", include("watson.urls", namespace="watson"))
	]

