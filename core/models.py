from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100, null=True, verbose_name='Your Name')
    email = models.EmailField(null=True, verbose_name='Your Email')
    subject = models.CharField(max_length=100, null=True)
    message = models.TextField(null=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=('name',))
        ]
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.name
