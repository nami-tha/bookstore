from django.db import models

# Create your models here.

class Books(models.Model):
    book_name=models.CharField(max_length=120,unique=True)
    author=models.CharField(max_length=120)
    price=models.PositiveIntegerField(default=50)
    description=models.CharField(max_length=250)
    active_status=models.BooleanField(default=True)
    image=models.ImageField(upload_to="images",null=True,blank=True)
    def __str__(self):
       return self.book_name