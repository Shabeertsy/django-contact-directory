from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    phone=models.IntegerField(unique=True,null=True)

    def __str__(self):
        return self.name
