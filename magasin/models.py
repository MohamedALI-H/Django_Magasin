from django.db import models
from datetime import date;

class Produit(models.Model):
    TYPE_CHOICES=[("em","emballé"),("fr","frais"),("cs","Conserve")]
    libellé=models.CharField(max_length=100)
    description=models.TextField()
    prix=models.DecimalField(max_digits=10,decimal_places=3)
    type=models.CharField(max_length=2,choices=TYPE_CHOICES,default="em")
    Img=models.ImageField(blank=True)
    catégorie=models.ForeignKey('Categorie',on_delete=models.CASCADE,null=True)
    Fournisseur=models.ForeignKey('Fournisseur',on_delete=models.CASCADE,null=True)

    def __str__(self):
        return "Description:"+str(self.description)+"Libélé"+str(self.libellé)+"prix:"+str(self.prix)+"Type:"+self.type

class Categorie(models.Model):
    TYPE_CHOICES=[('Al','Alimentaire'), ('Mb','Meuble'),('Sn','Sanitaire'), ('Vs','Vaisselle'),('Vt','Vêtement'),('Jx','Jouets'),('Lg','Linge de Maison'),('Bj','Bijoux'),('Dc','Décor')]
    name=models.CharField(max_length=50,default="Alimentaire",choices=TYPE_CHOICES)

    def __str__(self) -> str:
        return "Name: "+str(self.name)

class Fournisseur(models.Model):
    nom=models.CharField(max_length=100)
    adresse=models.TextField()
    email=models.EmailField()
    telephone=models.CharField(max_length=8)

    def __str__(self) -> str:
        return "Nom: "+str(self.nom)+" Adresse "+str(self.adresse)+" email: "+str(self.email)+" telephone: "+str(self.telephone)
    
class ProduitNC(Produit,models.Model):
    Duree_garantie=models.CharField(max_length=100)

    def str(self) -> str:
        return super().str() + " Duree_garantie: " + str(self.duree_garantie)
    
class Commande(models.Model):
    dateCde=models.DateField(null=True,default=date.today())
    totalCde=models.DecimalField(max_digits=10,decimal_places=3)
    Produits=models.ManyToManyField('Produit')
    def __str__(self) -> str:
        return "DateCDe: "+str(self.dateCde)+" TotalCde: "+str(self.totalCde)
    @property
    def description(self):

        return " ".join(str(p) for p in self.Produits.all())
    def total(self):
        total = 0
        for p in self.Produits.all():
            total += p.prix
        return total
    
# Create your models here.
