from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
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

    email = models.EmailField(verbose_name='email address',max_length=255)

    phone_regex = RegexValidator(regex=r'^\d{10}$',
                                 message="Phone number must be 10 digits and entered in the format: '1234567890'.")
    phone = models.CharField(validators=[phone_regex], max_length=10,
                             help_text="Format: 1234567890")
    can_text = models.BooleanField(
        verbose_name='By signing up, you consent to receive periodic text messages from When We All Vote (56005). Message and data rates may apply. Text HELP for more information. Text STOP to stop receiving messages.',
        default=False)

    utm_source = models.CharField(blank=True, max_length=100)
    utm_medium = models.CharField(blank=True, max_length=100)
    utm_campaign = models.CharField(blank=True, max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.first_name

class Mail(models.Model):
    street=models.CharField(max_length=100,verbose_name='Street Address')
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=2)
    zip=models.CharField(max_length=5,verbose_name='ZIP Code')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.street


class Zip(models.Model):
    zip=models.CharField(max_length=5)
    state=models.CharField(max_length=2)
    mail_only=models.CharField(max_length=100)
    link=models.URLField()

    def __str__(self):
        return self.zip