from django.urls import path,include
from . import views
urlpatterns = [
path('', views.vitrine,name='index'),
 path('nouvFournisseur/', views.nouveauFournisseur, name='nouveauFour'),
 path('commande/',views.commande, name='commande'),
 path('register/',views.register, name = 'register'),
 path("home/", views.home, name="home"),
 path('api/category/', views.CategoryAPIView.as_view()),
 path('api/product/', views.ProduitAPIView.as_view()),
path('vitrine/', views.vitrineFilter, name='vitrineFilter'),
path('api/product/<int:category_id>/',views.ProductViewset.as_view({'get': 'retrieve'}), name='product-detail'),
]