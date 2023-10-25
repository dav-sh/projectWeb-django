from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(null=False)
    message = models.CharField(max_length=200)

    class Meta():
        verbose_name = 'contacto'
        verbose_name_plural = 'contactos'
    def __str__(self) -> str:
        return self.name