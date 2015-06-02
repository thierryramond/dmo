from django.db import models


genre_list = (('M.','M.'),('Mme','Mme'),)
specialite_list = (('L3 MFA','L3 MFA'),('L3 MINT','L3 MINT'),('M1 MFA','M1 MFA'),('Magistère 1','Magistère 1'),('Magistère 2','Magistère 2'),('Magistère 3','Magistère 3'))
responsable_list = (('Dominique Hulin','Dominique Hulin'),('Marie-Anne Poursat','Marie-Anne Poursat'))


class Etudiant(models.Model):
    genre = models.CharField(db_column='genre',max_length=25, blank=True, null=True,choices=genre_list)
    nom = models.CharField(db_column='Nom', max_length=25, blank=True, null=True)
    prenom = models.CharField(db_column='Prenom', max_length=28, blank=True, null=True)
    date_naissance =  models.DateField(db_column="date_naissance",blank=True, null=True)
    adresse = models.CharField(db_column='adresse', max_length=100, blank=True, null=True)
    email = models.EmailField(db_column='email', unique=True, blank=True, null=True)
    telephone = models.CharField(db_column='telephone', max_length=100, blank=True, null=True)
    carte_etudiant = models.CharField(db_column='carte_etudiant',unique=True, max_length=10, blank=True, null=True)
    vient_de = models.CharField(db_column='vient_de', max_length=150, blank=True, null=True)
    
    class Meta:
        ordering = ('nom','prenom')

    def __str__(self):
        return '{0} {1}'.format(self.prenom, self.nom)

    def get_value(self):
        return [(field.value(self)) for field in Etudiant._meta.get_fields(include_hidden=False)]

    def get_annee(self):
        return (Annee.objects.filter(etudiant=self)).order_by('millesime')

class Candidature(models.Model):
    etudiant = models.ForeignKey(Etudiant)
    date_demande = models.DateField(db_column='date_demande', blank=True, null=True)
    demande = models.CharField(db_column='demande', max_length=50, blank=True, null=True, choices=specialite_list)
    reponse = models.CharField(db_column='reponse', max_length=50, blank=True, null=True,choices=specialite_list)
    confirmation = models.CharField(db_column='confirmation',max_length=50, blank=True, null=True,choices=specialite_list)
    reponse_donnee_par = models.CharField(db_column='reponse_donnee_par',max_length=50, blank=True, null=True,choices=responsable_list)
    date_reponse = models.DateField(db_column='date_reponse', blank=True, null=True)
    numero_OPI = models.CharField(db_column='numero_OPI', max_length=10, blank=True, null=True)

class Annee(models.Model):
    etudiant = models.ForeignKey(Etudiant)
    millesime  = models.CharField(db_column='millesime', max_length=30, blank=True, null=True)
    etablissement = models.CharField(db_column='etablissement', max_length=100, blank=True, null=True)
    formation = models.CharField(db_column='formation', max_length=100, blank=True, null=True)
    resultat = models.CharField(db_column='resultat', max_length=30, blank=True, null=True)



