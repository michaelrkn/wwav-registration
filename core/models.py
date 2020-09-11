from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.



def validate_zip(value):
    try:
        v = Zip.objects.get(zip=value)
    except Zip.DoesNotExist:
        raise ValidationError("Please enter a valid ZIP code.")


class Registration(models.Model):
    first_name=models.CharField(max_length=100,verbose_name='First Name')
    last_name=models.CharField(max_length=100,verbose_name='Last Name')
    zip=models.CharField(max_length=5,verbose_name='ZIP Code',validators=[validate_zip])

    utm_source = models.CharField(blank=True, max_length=100)
    utm_medium = models.CharField(blank=True, max_length=100)
    utm_campaign = models.CharField(blank=True, max_length=100)


    def __str__(self):
        return self.first_name

class Mail(models.Model):
    street=models.CharField(max_length=100,verbose_name='Street Address')
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=2)
    zip=models.CharField(max_length=5,verbose_name='ZIP Code')

    def __str__(self):
        return self.street


class Zip(models.Model):
    zip=models.CharField(max_length=5)
    state=models.CharField(max_length=2)
    mail_only=models.BooleanField()
    link=models.URLField()

    def __str__(self):
        return self.zip