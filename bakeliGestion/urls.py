from django.db import router
from django.urls import include, path
from bakeliGestion import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'user',views.UserViewSet, basename='user')
router.register(r'eleve', views.EleveViewSet, basename='eleve')
router.register(r'etablissement', views.EtablissementViewSet,basename='etablissement')
router.register(r'entreprise', views.EntrepriseViewSet, basename='entreprise')

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/signup/<int:pk>/',views.typeSignUp, name='typeSignup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/offre', views.add_offre, name='offre'),
    path('api/', include(router.urls)),
]