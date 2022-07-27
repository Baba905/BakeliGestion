from cmath import e
from django.shortcuts import redirect, render
#from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from bakeliGestion import forms
from bakeliGestion import models
from bakeliGestion import serializers
from django.contrib.auth import get_user_model
User = get_user_model()

def home(request):
    return render(request,'home.html',{    
    })

def signup(request):
    #form= forms.SignUpForm()
    if request.method=='POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user= User.objects.last()
            return redirect('./'+str(user.id)+'/')
    else:
        form= forms.SignUpForm()
    return render(request, 'registration/signup.html',{'form': form})

def etablissement_signup(request):
    if request.method=='POST':
            form= forms.EtablissementSignUp(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
    else:
            form = forms.EtablissementSignUp()
            return render(request,'etablissement.html',{'form':form})


def entreprise_signup(request):
    if request.method=='POST':
            form= forms.EntrepriseSignUp(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
            else:
                return redirect('signup')
    else:
            form = forms.EntrepriseSignUp()
            return render(request,'entreprise.html',{'form':form})

def eleve_sinup(request):
    if request.method=='POST':
            form= forms.EleveSignUp(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
            else:
                return redirect('signup')
    else:
        form =forms.EleveSignUp()
        return render(request,'eleve.html', {'form': form})
  

def typeSignUp(request,pk):
    user = models.User.objects.get(pk=pk)

    if user.user_type==1:
        etablissement_signup(request)
    elif user.user_type==2:
       eleve_sinup(request)
    elif user.user_type==3:
        entreprise_signup(request)
    else:
        return render(request,'home.html',{})

def add_offre(request):
    if request.method=='POST':
        form = forms.OffreAdd(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = forms.OffreAdd()
        return render(request, 'offre.html', {'form': form})

def view_offre(request):
    offres = models.Offre.objects.all()
    return render(request,'home.html', {'offres': offres})

class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

class EleveViewSet(viewsets.ModelViewSet):
    queryset=models.Eleve.objects.all()
    serializer_class = serializers.EleveSerializer
    #permission_classes = [permissions.IsAuthenticated]

class EtablissementViewSet(viewsets.ModelViewSet):
    queryset= models.Etablissement.objects.all()
    serializer_class = serializers.EtablissementSerializer

class EntrepriseViewSet(viewsets.ModelViewSet):
    queryset = models.Entreprise.objects.all()
    serializer_class = serializers.EntrepriseSerializer