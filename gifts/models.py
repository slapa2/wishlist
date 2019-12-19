from django.db import models

# Create your models here.
class GiftsList(models.Model):
    name = models.CharField(max_length=200) 

class Gift(models.Model):
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    img_url = models.CharField(max_length=400)
    gift_list = models.ForeignKey(GiftsList, on_delete=models.CASCADE)

class GiftUrl(models.Model):
    url = models.CharField(max_length=400)
    gift = models.ForeignKey(Gift, on_delete=models.CASCADE)