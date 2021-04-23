from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.


class Card(models.Model): #creating model and the fields needed
    image = models.ImageField(max_length = 200)
    qoute = models.CharField(max_length = 50)
    date = models.DateTimeField(auto_now_add= True)


#to delete image from media file when you delete object from admin.
@receiver(post_delete, sender=Card)
def photo_post_delete_handler(sender, **kwargs):
    photo = kwargs['instance']
    storage, path = photo.image.storage, photo.image.path
    storage.delete(path)
