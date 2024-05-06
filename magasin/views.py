from django.shortcuts import render
from django.template import loader
from .models import Produit,Fournisseur,Commande,Categorie
from .forms import FournisseurForm, ProduitForm,CommandeForm,UserRegistrationForm,UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.http import HttpResponseBadRequest,HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.views import APIView
from rest_framework.response import Response
from magasin.serializers import CategorySerializer,ProductSerializer
from rest_framework import viewsets
# Create your views here.

@login_required
def home(request):
    context={'val':"Menu Acceuil"}
    return HttpResponse("Hello, World!")
    '''return render(request,'home.html',context)'''

def vitrine(request):
    list=Produit.objects.all()
    return render(request,'magasin/vitrine.html',{'list':list})
@login_required
def index(request):
    return render(request,'magasin/acceuil.html')

def nouveauFournisseur(request):
    fournisseurs = Fournisseur.objects.all()
    if request.method == 'POST':
        form = FournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nouveauFour')
    else:
        form = FournisseurForm()
    return render(request, 'magasin/fournisseur.html', {'form': form,'Fournisseurs':fournisseurs})


def commande(request):
    commandes = Commande.objects.all()
    
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            form.save()
           
    else:
        form = CommandeForm()

    context = {'form': form, 'commandes': commandes}
    return render(request, 'magasin/Commande.html', context)

def register(request):
    if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, f'Coucou {username}, Votre compte a étécréé avec succès !')
            return redirect('home')
    else :
        form = UserCreationForm()
        return render(request,'registration/register.html',{'form' : form})



    # Redirect to a success page.
class CategoryAPIView(APIView):
    def get(self, *args, **kwargs):
        categories = Categorie.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
class ProduitAPIView(APIView):
    def get(self, *args, **kwargs):
        produits = Produit.objects.all()
        serializer = ProductSerializer(produits, many=True)
        return Response(serializer.data)

class ProductViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    def get_queryset(self):
        queryset = Produit.objects.all()
        category_id = self.request.GET.get('category_id')
        if category_id:     
            queryset = queryset.filter(categorie_id=category_id)
        return queryset

def vitrineFilter(request):
    libelle = request.GET.get('libelle')  # renamed to match the form input name
    list = Produit.objects.filter(libellé__icontains=libelle)  # use icontains for case-insensitive search
    return render(request, 'magasin/vitrine.html', {'list': list})  # renamed to produits

def handler404(request, exception):
    return render(request, 'magasin/404.html', status=404)