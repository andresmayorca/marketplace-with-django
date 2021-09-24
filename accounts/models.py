from django.db import models
from django.contrib.auth.models import AbstractUser
from marketplace.models import Product
# Create your models here.

class User(AbstractUser):
    stripe_customer_id = models.CharField(max_length=50)

class UserLibrary(models.Model)
    user models.OneToOneField(User, on_delete=models.CASCADE, related_name="library")
    products = models.ManyToManyField("Product", blank=True)

    def __str__(self):
        return self.user.email
     