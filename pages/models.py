from django.db import models

class Contact(models.Model):
    Ad = models.CharField(max_length=100)
    Soyad = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    Telefon = models.CharField(max_length=100)
    mesaj = models.TextField(blank=True)

    def __str__(self):
        return self.email
