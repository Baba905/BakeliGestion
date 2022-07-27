from dataclasses import field
from pyexpat import model
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from bakeliGestion.models import User, Etablissement, Eleve, Entreprise,Offre
from django.contrib.auth import get_user_model
User = get_user_model()


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=63)
    #password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')
    # user_type = forms.ChoiceField(choices=User.USER_TYPE_CHOICES)
    class Meta :
        model = User
        fields = ('username','email','password1','password2', 'user_type')

class EtablissementSignUp(ModelForm):
    class Meta:
        model = Etablissement
        fields =('nom', 'adresse','user')
    

class EleveSignUp(ModelForm):
    
    class Meta :
        model = Eleve
        fields= ('user', 'nom', 'prenom','niveau','etablissement' )
    

class EntrepriseSignUp(ModelForm):
    class Meta:
        model = Entreprise
        fields= ('user', 'nom', 'adresse', 'numeroSiret', 'secteur')

class OffreAdd(ModelForm):
    class Meta:
        model = Offre
        fields= ('titre', 'details', 'entreprise')