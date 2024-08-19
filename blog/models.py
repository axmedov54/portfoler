from django.db import models

# Create your models here.

class Books(models.Model):
    title= models.CharField(max_length=25)
    image= models.ImageField(upload_to="Kitoblar / rasm",null=True)
    price=models.PositiveBigIntegerField()
    malumot=models.TextField()


