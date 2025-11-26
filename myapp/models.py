from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100 , null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    subject = models.TextField()
    message = models.CharField(max_length=200)
    def __str__(self):
        return self.name