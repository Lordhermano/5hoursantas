from django.db import models

# Create your models here.
class Destination(models.Model):
    '''This model is used to auto generate the content for a particular holiday 
    and save the images in the database so they could be used by any user.
    
    This makes sure the images and other data are not lost went sending them 
    to the user.'''
    main_img = models.ImageField(upload_to='static/images/')
    second_img = models.ImageField(upload_to='static/images/')
    Title = models.CharField(max_length=20)
    Overview_desc = models.CharField(max_length=1000)
    Travel_Guide_desc = models.CharField(max_length=1000,default=0)
    Things_to_do_desc = models.CharField(max_length=1000,default=0)
    adult_price = models.CharField(max_length=20)
    children_price = models.CharField(max_length=20)
    infants_price = models.CharField(max_length=20)