from django.apps import AppConfig
import watson

class ApplyConfig(AppConfig):
    name = "Apply"
    def ready(self):
        etudiant = self.get_model("Etudiant")
        candidature = self.get_model("Candidature")
        watson.register(etudiant,candidature)