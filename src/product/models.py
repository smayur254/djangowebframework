from django.db import models
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    rate = models.DecimalField(max_digits=111111111, decimal_places=2)
    feature = models.BooleanField(default=False)

    
    def get_absolute_url(self):
        # return f"/prodct/{self.id}"  
        return reverse("productDetail", args=[self.id])
    
    
