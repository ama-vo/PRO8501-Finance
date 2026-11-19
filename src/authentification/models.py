from django.contrib.auth.models import AbstractUser
from django.db import models



class FinanceUser(AbstractUser):
    # Ajoutez vos champs personnalisés ici
  
  # Django crée automatiquement l'id. 
  # id = models.AutoField(primary_key=True)
  
  # Déjà présent dans AbstractUser. 
  # mail = models.EmailField()
  # nom = models.CharField(max_length=100)
  # prenom = models.CharField(max_length=100)

  pays = models.CharField(max_length=100, default="France")
  adresse = models.CharField(max_length=255)
  telephone = models.CharField(max_length=20)
  riskProfile = { 1, 2, 3, 4, 5 } 


class Emplacement(models.Model):
    
  nom = models.CharField(max_length=100)
  pays = models.CharField(max_length=100, default="France")
  type = models.CharField(max_length=100, choices=[
    ("Banque"),
    ("Courtier"),
    ("Assureurs"),
    ("Sociétés de gestion"),
    ("Plateformes FinTech"),
  ])
